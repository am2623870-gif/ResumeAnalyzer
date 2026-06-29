from flask import (
    Flask,
    render_template,
    request,
    send_file,
    redirect,
    session
)
from resume_parser import extract_text
from skills import extract_skills
from similarity import calculate_similarity
from ats import calculate_ats_score
from suggestions import generate_suggestions
from gemini_feedback import get_feedback
from database import (
    init_db,
    create_users_table,
    register_user,
    get_user_by_email,
    save_analysis,
    get_history,
    get_total_analyses,
    get_average_ats,
    get_best_ats,
    get_rankings
)
from pdf_generator import generate_pdf
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import os
import time

app = Flask(__name__)
UPLOAD_FOLDER= "uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

app.secret_key = os.getenv(
    "SECRET_KEY",
    "resume_analyzer_secret"
)

init_db()
create_users_table()

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "index.html",
        username=session["user"]
    )

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]

        password = generate_password_hash(
    request.form["password"],
    method="pbkdf2:sha256"
)

        try:

            register_user(
                username,
                email,
                password
            )

            return redirect("/login")

        except:

            return "User already exists"

    return render_template(
        "register.html"
    )

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)

        if user and check_password_hash(
            user[3],
            password
        ):

            session["user"] = user[1]

            return redirect("/")

        return "Invalid Email or Password"

    return render_template(
        "login.html"
    )

@app.route("/logout")
def logout():

    session.pop(
        "user",
        None
    )

    return redirect("/login")


@app.route("/history")
def history():

    records = get_history()

    html = """
    <html>
    <head>
        <title>Analysis History</title>

        <style>
            body{
                font-family: Arial;
                padding:40px;
            }

            table{
                border-collapse: collapse;
                width:100%;
            }

            th,td{
                border:1px solid #ccc;
                padding:10px;
                text-align:center;
            }

            th{
                background:#f4f4f4;
            }
        </style>

    </head>

    <body>

    <h1>Resume Analysis History</h1>

    <table>

        <tr>
            <th>Resume Name</th>
            <th>ATS Score</th>
            <th>AI Score</th>
            <th>Date</th>
        </tr>
    """

    for row in records:

        html += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
        </tr>
        """

    html += """

    </table>

    <br><br>

    <a href="/">
        Back to Home
    </a>

    </body>
    </html>
    """

    return html

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    total = get_total_analyses()
    avg_ats = get_average_ats()
    best_ats = get_best_ats()

    return render_template(
        "dashboard.html",
        total=total,
        avg_ats=avg_ats,
        best_ats=best_ats
    )



@app.route("/rankings")
def rankings():

    if "user" not in session:
        return redirect("/login")

    ranking_data = get_rankings()

    return render_template(
        "rankings.html",
        rankings=ranking_data
    )


@app.route("/download/<filename>")
def download(filename):

    return send_file(
        os.path.join(
            "uploads",
            filename
        ),
        as_attachment=True
    )


@app.route("/upload", methods=["POST"])
def upload():

    if "user" not in session:
        return redirect("/login")

    file = request.files["resume"]

    if not file:
        return "No file selected"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    file.save(filepath)

    # Extract Resume Text
    resume_text = extract_text(filepath)

    # Job Description
    job_description = request.form[
        "job_description"
    ]

    # AI Similarity
    ai_score = calculate_similarity(
        resume_text,
        job_description
    )

    # Skills
    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )
    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)

    # Matched Skills
    matched = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    # Missing Skills
    missing = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    # Skill Match Score
    if len(jd_skills) > 0:

        skill_score = (
            len(matched)
            /
            len(jd_skills)
        ) * 100

    else:

        skill_score = 0

    # ATS Score
    ats_score = calculate_ats_score(
        skill_score,
        ai_score,
        resume_text
    )

    # Save to Database
    save_analysis(
        file.filename,
        ats_score,
        ai_score
    )

    # Suggestions
    suggestions = generate_suggestions(
        missing,
        ats_score
    )

    suggestion_html = ""

    for suggestion in suggestions:

        suggestion_html += (
            f"<li>{suggestion}</li>"
        )

    # Gemini Feedback
    try:

        ai_feedback = get_feedback(
            resume_text,
            job_description
        )

    except Exception:

       ai_feedback = """
    AI feedback temporarily unavailable.

    Possible reasons:
    • Gemini quota exceeded
    • Invalid API key
    • Network issue

    Please try again later.
   """

    # Generate PDF
    pdf_filename = (
        "report_"
        + str(int(time.time()))
        + ".pdf"
    )

    pdf_path = os.path.join(
        "uploads",
        pdf_filename
    )

    generate_pdf(
        pdf_path,
        ats_score,
        ai_score,
        matched,
        missing,
        ai_feedback
    )

    return render_template(
    "result.html",
    ats_score=ats_score,
    skill_score=skill_score,
    ai_score=ai_score,
    resume_skills=resume_skills,
    jd_skills=jd_skills,
    matched=matched,
    missing=missing,
    suggestions=suggestions,
    ai_feedback=ai_feedback,
    pdf_filename=pdf_filename
)


if __name__ == "__main__":
    app.run(debug=True)