from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(
    filename,
    ats_score,
    ai_score,
    matched,
    missing,
    feedback
):

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats_score}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"AI Score: {ai_score}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Matched Skills: {matched}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Missing Skills: {missing}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Gemini Feedback",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            feedback,
            styles["Normal"]
        )
    )

    pdf.build(content)