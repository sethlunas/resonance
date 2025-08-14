# resonance
Project Resonance

# Resonance - ATS Resume Analyzer

A web application that analyzes how well your resume matches a specific job description. Upload your resume, paste a job listing, and get a compatibility score with suggestions for improvement.

## 🎯 What it does
- Parses resumes (PDF/DOCX) and job descriptions
- Extracts and compares keywords/skills
- Calculates a Fit Score (0-100) using TF-IDF similarity
- Shows matched vs missing keywords
- Suggests resume improvements

## 🛠 Tech Stack
- **Backend:** Python, Flask, spaCy, scikit-learn
- **Frontend:** React + Vite
- **File Processing:** PyPDF2, python-docx

## 🚀 Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
