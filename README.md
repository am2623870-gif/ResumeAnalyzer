# 🚀 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Flask**, **Google Gemini AI**, and **Machine Learning** that evaluates resumes against job descriptions, calculates ATS scores, ranks resumes, and generates AI-powered feedback.

---

## 📌 Features

### 👤 User Authentication
- User Registration
- User Login
- Secure Password Hashing
- Session Management

### 📄 Resume Analysis
- Upload Resume (PDF)
- Resume Text Extraction
- ATS Score Calculation
- AI Similarity Score
- Resume Ranking
- Skill Extraction
- Matched Skills Detection
- Missing Skills Detection
- Resume Improvement Suggestions

### 🤖 AI Integration
- Google Gemini AI Feedback
- Resume Improvement Tips
- ATS Optimization Advice
- Interview Preparation Suggestions

### 📊 Dashboard
- Total Resume Analyses
- Average ATS Score
- Best ATS Score
- Interactive Chart.js Dashboard

### 📑 Reports
- Generate Professional PDF Report
- Download Analysis Report

### 🗂 History
- Resume Analysis History
- Stored Using SQLite Database

---

# 🛠 Technologies Used

## Backend
- Python
- Flask

## Database
- SQLite3

## Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## AI
- Google Gemini API

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Chart.js
- Jinja2

## PDF Processing
- pdfplumber
- ReportLab

---

# 📁 Project Structure

```
ResumeAnalyzer/
│
├── app.py
├── database.py
├── ats.py
├── similarity.py
├── skills.py
├── suggestions.py
├── resume_parser.py
├── gemini_feedback.py
├── pdf_generator.py
├── requirements.txt
├── README.md
├── .env
├── uploads/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── result.html
│   ├── dashboard.html
│   ├── ranking.html
│
├── static/
│   ├── css/
│   └── images/
│
└── resume_analyzer.db
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ResumeAnalyzer.git
```

```bash
cd ResumeAnalyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
python3 -m pip install -r requirements.txt
```

---

# 🔑 Configure Gemini API

Create a file named

```
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can get a free API key from:

https://aistudio.google.com/app/apikey

---

# ▶ Run the Application

```bash
python app.py
```

or

```bash
python3 app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 📊 Workflow

```
User Login
      │
      ▼
Upload Resume (PDF)
      │
      ▼
Extract Resume Text
      │
      ▼
Enter Job Description
      │
      ▼
TF-IDF Similarity Calculation
      │
      ▼
Skill Extraction
      │
      ▼
ATS Score Calculation
      │
      ▼
Gemini AI Feedback
      │
      ▼
Generate PDF Report
      │
      ▼
Store Results in SQLite
      │
      ▼
Dashboard & Ranking
```

---

# 📈 ATS Score Formula

```
ATS Score =
40% Skill Match +
30% AI Similarity +
20% Resume Length +
10% Resume Sections
```

---

# 📷 Screenshots

Add screenshots after deployment.

Examples:

```
Home Page

Login Page

Resume Analysis

Dashboard

Resume Ranking

PDF Report
```

---

# 🎯 Future Improvements

- Drag & Drop Resume Upload
- Multiple Resume Comparison
- Resume Templates
- Dark Mode
- AI Chat Assistant
- Email PDF Report
- Cloud Database
- Docker Deployment
- Admin Dashboard

---

# 🚀 Deployment

The project can be deployed on:

- Render
- Railway
- PythonAnywhere

---

# 👨‍💻 Author

**Aman Mishra**

B.Tech Computer Science Engineering

ITER, Siksha 'O' Anusandhan University

---

# ⭐ If you like this project

Please give it a ⭐ on GitHub.