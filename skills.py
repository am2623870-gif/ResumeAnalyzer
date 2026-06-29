skills_db = [

    "python",
    "java",
    "c",
    "c++",

    "html",
    "css",
    "javascript",
    "typescript",

    "react",
    "angular",
    "vue",

    "nodejs",
    "express",

    "flask",
    "django",
    "fastapi",

    "mysql",
    "postgresql",
    "mongodb",
    "sql",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "gcp",

    "git",
    "github",

    "machine learning",
    "deep learning",

    "tensorflow",
    "pytorch",

    "numpy",
    "pandas",

    "data structures",
    "algorithms",

    "operating systems",

    "computer networks",

    "oop",

    "linux"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found