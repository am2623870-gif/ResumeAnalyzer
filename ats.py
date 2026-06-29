def calculate_ats_score(
    skill_score,
    ai_score,
    resume_text
):

    # Resume length score
    words = len(resume_text.split())

    if words >= 300:
        length_score = 100
    elif words >= 200:
        length_score = 80
    else:
        length_score = 50

    # Section score
    sections = [
        "education",
        "skills",
        "project",
        "experience"
    ]

    found = 0

    resume_lower = resume_text.lower()

    for section in sections:

        if section in resume_lower:
            found += 1

    section_score = (
        found /
        len(sections)
    ) * 100

    ats_score = (
        skill_score * 0.4 +
        ai_score * 0.3 +
        length_score * 0.2 +
        section_score * 0.1
    )

    return round(ats_score, 2)