# Project Resonance — ATS/JD/Resume Keyword Analyzer

**Owner:** Syn  
**Goal:** Evaluate resume ↔ job description alignment with a transparent Fit Score, keyword gaps, and rewrite suggestions.

---

## Features
- Upload resume (PDF/DOCX) + paste job description  
- Extract and preprocess text  
- Keyword coverage analysis (matched vs missing)  
- TF-IDF similarity scoring  
- Combined **Fit Score (0–100)**  
- Actionable suggestions for resume improvements  

---

## Tech Stack
- **Backend:** Python 3, Flask, Pydantic  
- **NLP/Scoring:** spaCy, scikit-learn (TF-IDF + cosine), pandas  
- **Frontend:** React + Vite (Tailwind optional)  
- **Storage:** Local FS (MVP, no DB)  
- **Optional AI:** OpenAI API for rewrite suggestions  

---

## Quick Start

## Backend
``` bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```
- this will run locally on http://localhost:5000 as that is the default server for Flask

## Frontend
``` bash
cd frontend
npm install
npm run dev
```
- this will run locally on http://localhost:3000 as that is the default server for React

---

## Documentation

- See the docs/ folder for detailed information:
  - [blueprint.md](./docs/blueprint.md) - vision, workflow, scoring model
  - [master_checklist.md](./docs/master_checklist.md) - technical order, step-by-step build plan

---

### Status

- [X] Repo + scaffold
- [X] Basic Flask app + file upload
- [ ] Text extraction engine (current phase)
- [ ] Core analysis (TF-IDF + skills coverage)
- [ ] API + React frontend
- [ ] Fit Score with matched/missing breakdown

--- 

### Disclaimer

_This project is being built as a learning + portfolio project. Both planning and parts of the coding (e.g., Flask, file scaffolding, file upload) were AI-assisted. I am using AI (specifically chatGPT and claude) as a coding partner while I learn the stack. All design decisions, documentation, integration work, and ongoing development are my own and I am incrementally learning the implementation details along the way._

_Note: Some parts of the code are intentionally commented more heavily than normal. These comments reflect concepts I am learning (e.g., how Flask routes work) and serve as a personal learning aid. They may be pruned or refactored in later versions of the project._

---
