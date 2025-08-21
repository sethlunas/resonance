# 🧭 ATS/JD/Resume Keyword Analyzer — Project Resonance
**Owner:** Syn  
**Goal:** Evaluate resume ↔ job description alignment with a transparent Fit Score, keyword gaps, and rewrite suggestions.  

- ATS stands for **Applicant Tracking System**, which is software used by employers to manage the recruitment and hiring process, including job postings, resume collection, and candidate tracking. It helps streamline hiring by organizing applicant information and automating various tasks.
  [![](https://external-content.duckduckgo.com/ip3/www.techtarget.com.ico)](https://www.techtarget.com/searchhrsoftware/definition/applicant-tracking-system-ATS)

_Disclaimer: This document was initially AI-assisted but is actively maintained as the authoritative project blueprint._

---

## 1) 🎯 Project Overview
Web app that:
- Ingests a **resume (PDF/DOCX)** + **job description (JD text)**.
- Parses skills/keywords, computes similarity + coverage.
- Outputs a **Fit Score (0–100)** and **actionable suggestions**.

---

## 2) 🙋 User Workflow (How you’ll use it)
1. **Find a JD** on LinkedIn/Indeed/company site → copy the full description.
2. **Open the tool** (local `localhost` during MVP).
3. **Upload your resume** (PDF/DOCX).
4. **Paste the JD** into the text area (optionally choose role profile to tweak weights).
5. **Click Analyze** → backend computes:
   - Keyword coverage (required/preferred)
   - TF-IDF cosine similarity
   - Blended **Fit Score**
   - Matched vs Missing with weights + rewrite ideas
6. **Edit resume** to cover missing essentials (naturally, truthfully).
7. **Re-run (optional)** until score/coverage hits your threshold → apply.

---

## 3) 📌 Objectives
1. **MVP fast**: Local Flask + React app that reliably returns Fit Score + gaps.
2. **Explainability**: Show *why* the score is what it is (weights, matches, misses).
3. **InternScout synergy**: Provide JSON output to feed future automation.
4. **SaaS-ready shape**: Clean module boundaries for easy cloud deploy later.

---

## 4) 🛠 Tech Stack
- **Backend:** Python 3, Flask, Pydantic (schemas)
- **NLP/Scoring:** spaCy (tokenize/lemmatize/NER), scikit-learn (TF-IDF, cosine), pandas
- **Frontend:** React + Vite, (Tailwind optional)
- **Optional AI:** OpenAI for rewrite phrasing/synonym hints (toggleable)
- **Storage:** Local FS (no DB for MVP)

---

## 5) 🧮 Scoring Model (transparent)
**Signals**
- Skills/Core tech (python, c++, numpy, react)
- Tools/Frameworks (flask, fastapi, docker, aws)
- Role nouns (backend, ml, security)
- Certs (security+, aws cp)

**Weights (example)**
- Present **required**: +3
- Present **preferred**: +1
- Missing **required**: −3
- Missing **preferred**: −1

**Blend**
- `fit = 0.6 * skills_coverage + 0.4 * (tfidf_cosine * 100) -> clamp 0-100`

**Outputs**
- Top matched (with weights)
- Top missing (with suggested phrasing)
- Section tips (Skills / Experience bullets)

---

## 6) 📅 Development Roadmap (MVP-first)

### Phase 1 — Core Engine (Day 1–2)
- [ ] PDF/DOCX → text extractors
- [ ] Tokenize/lemmatize/stopword removal
- [ ] `skills_map.json` (canonical skills + simple synonyms)
- [ ] TF-IDF vectors + cosine sim
- [ ] Skills coverage scoring + blend → Fit Score

### Phase 2 — API Layer (Day 2–3)
- [ ] Flask `/score` (file upload + JD text)
- [ ] Response JSON: `{ fit_score, matched[], missing[], weights, suggestions[] }`
- [ ] Unit tests with 3–5 real JDs + sample resume

### Phase 3 — UI (Day 3–4)
- [ ] React form: upload resume, paste JD, role profile dropdown
- [ ] Results panel: big score, chips for matched/missing, suggestion bullets

### Phase 4 — Explainability & Polish (Day 5)
- [ ] Weighted table + reason string
- [ ] (Optional) OpenAI rewrite for 2–3 bullets
- [ ] Export: save result JSON/markdown

### Phase 5 — Ship (Day 5–6)
- [ ] `run_local.sh` (backend + frontend)
- [ ] README demo steps
- [ ] (Optional) Deploy to Render/Railway for shareable demo

---

## 7) 🧠 Stretch (post-MVP)
- Smarter synonyms via embeddings/OpenAI
- Resume section detection (Edu/Exp/Skills)
- Batch scoring across multiple JDs
- Per-role calibration profiles (SWE, Security, AI)
- History + profiles when you add a DB

---

## 8) 📄 Resume Entry (draft)
**ATS Fit Scanner — Resume ↔ JD Analyzer**  
- Built Flask/React tool that scores alignment using weighted keyword coverage + TF-IDF similarity with transparent explainability  
- Generated matched/missing lists and rewrite suggestions for targeted applications  
- Tech: Python, Flask, spaCy, scikit-learn, React, Pandas, (OpenAI optional)

---

## 9) 🗂 File Structure (planned)

<pre>
ats-fit-scanner/
│── backend/
│   ├── app.py               # Flask app, /score route
│   ├── scoring.py           # TF-IDF + coverage blend
│   ├── extract.py           # PDF/DOCX → text
│   ├── skills_map.json      # canonical skills + synonyms
│   └── schemas.py           # Pydantic request/response
│── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/ResultPanel.jsx
│   │   └── api.js
│   └── index.html
│── tests/
│   ├── samples/
│   │   ├── resume_sample.pdf
│   │   └── jd_sample_*.txt
│   └── test_scoring.py
│── README.md
│── run_local.sh
</pre>

---

## 10) ✅ Success Criteria
- Analyze resume + pasted JD → **Fit Score** returned in <3s locally
- Clear matched/missing with weights + 2–3 actionable suggestions
- JSON export for InternScout integration
- Works fully offline when OpenAI features are toggled off

---

## 11) 🔧 Quick Start (after scaffold)

```
bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install flask pydantic spacy scikit-learn pandas python-docx pypdf2
python -m spacy download en_core_web_sm
python app.py

# Frontend
cd ../frontend
npm i && npm run dev
```


