import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_feedback(
    resume_text,
    job_description
):

    prompt = f"""
    Analyze this resume against
    the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:

    1. Missing skills
    2. Resume improvements
    3. ATS improvements
    4. Interview preparation advice

    Keep response concise.
    """

    response = model.generate_content(
        prompt
    )

    return response.text
