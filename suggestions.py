def generate_suggestions(
    missing_skills,
    ats_score
):

    suggestions = []

    if ats_score < 60:
        suggestions.append(
            "Resume needs major improvements."
        )

    elif ats_score < 80:
        suggestions.append(
            "Resume is decent but can be improved."
        )

    else:
        suggestions.append(
            "Resume is ATS friendly."
        )

    for skill in missing_skills:

        suggestions.append(
            f"Add or learn {skill}"
        )

    return suggestions