from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    return similarity[0][0] * 100