import sqlite3


# =========================
# ANALYSIS TABLE
# =========================

def init_db():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        resume_name TEXT NOT NULL,

        ats_score REAL,

        ai_score REAL,

        date TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


# =========================
# USERS TABLE
# =========================

def create_users_table():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()


# =========================
# USER FUNCTIONS
# =========================

def register_user(
    username,
    email,
    password
):

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password
        )

        VALUES
        (?, ?, ?)
        """,
        (
            username,
            email,
            password
        )
    )

    conn.commit()
    conn.close()


def get_user_by_email(email):

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_username(username):

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# =========================
# ANALYSIS FUNCTIONS
# =========================

def save_analysis(
    resume_name,
    ats_score,
    ai_score
):

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis
        (
            resume_name,
            ats_score,
            ai_score
        )

        VALUES
        (?, ?, ?)
        """,
        (
            resume_name,
            ats_score,
            ai_score
        )
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

        resume_name,
        ats_score,
        ai_score,
        date

        FROM analysis

        ORDER BY id DESC
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records


# =========================
# DASHBOARD FUNCTIONS
# (Used in next phase)
# =========================

def get_total_analyses():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analysis
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_average_ats():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(ats_score)
        FROM analysis
        """
    )

    result = cursor.fetchone()[0]

    conn.close()

    if result is None:
        return 0

    return round(
        result,
        2
    )


def get_best_ats():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT MAX(ats_score)
        FROM analysis
        """
    )

    result = cursor.fetchone()[0]

    conn.close()

    if result is None:
        return 0

    return round(
        result,
        2
    )


def delete_all_history():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM analysis
        """
    )

    conn.commit()
    conn.close()

def get_total_analyses():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM analysis"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_average_ats():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(ats_score) FROM analysis"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return round(result or 0, 2)


def get_best_ats():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT MAX(ats_score) FROM analysis"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return round(result or 0, 2)

def get_rankings():

    conn = sqlite3.connect(
        "resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            resume_name,
            ats_score
        FROM analysis
        ORDER BY ats_score DESC
    """)

    rankings = cursor.fetchall()

    conn.close()

    return rankings