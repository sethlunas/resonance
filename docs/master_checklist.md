# 🧱 Project Resonance 
*ATS/JD/Resume Keyword Analyzer*

---

## 📂 Phase 0 — Foundation (already done ✅)
- [x] Create GitHub repo `resonance`  
- [x] Scaffold folders:  
  ```
  backend/
  frontend/
  tests/
  ```
- [x] Setup Python virtual environment in `backend/`  
- [x] Basic Flask “hello world” app runs  
- [x] File upload form works for PDF/DOCX  
- [x] Uploaded file validation + error handling  

---

## 📜 Phase 1 — Text Extraction Engine
**Goal:** Resume goes in → raw text comes out.  

1. **Install libraries**  
   - Add `pypdf2` (PDF) and `python-docx` (DOCX) to `requirements.txt`  
   - Install them inside your venv  

2. **Build extractor functions**  
   - One for PDF → returns plain text string  
   - One for DOCX → returns plain text string  

3. **Integrate with upload**  
   - Detect file type → call the right extractor  
   - Print or return extracted text (doesn’t need to look nice yet)  

4. **Display on page**  
   - After upload, show extracted text in a simple `<pre>` block in the webpage  

5. **Job Description input**  
   - Add textarea box to the upload page  
   - Allow user to paste JD text  
   - Display both resume + JD side by side  

✅ **Milestone:** You can see resume text + JD text on screen.

---

## 🧮 Phase 2 — Core Analysis Engine
**Goal:** Compute similarity + keyword coverage.  

1. **Preprocessing**  
   - Add `spacy` + English model (`en_core_web_sm`)  
   - Build text cleaning: lowercase, strip punctuation, stopword removal  
   - Lemmatization (normalize words: “running” → “run”)  

2. **Skills Map**  
   - Create `skills_map.json` with 20–30 seed skills + synonyms (e.g., "python", "c++", "aws", "docker")  

3. **Keyword Coverage**  
   - Check which skills exist in resume vs JD  
   - Count matches + misses  

4. **TF-IDF Similarity**  
   - Install `scikit-learn`  
   - Convert resume + JD into TF-IDF vectors  
   - Compute cosine similarity  

5. **Blend into Fit Score**  
   - Use formula:  
     `fit = 0.6 * skill_coverage + 0.4 * (cosine_similarity * 100)`  
   - Clamp 0–100  

✅ **Milestone:** Command-line prints Fit Score + matched/missing keywords.

---

## 🌐 Phase 3 — API Layer
**Goal:** Backend becomes a service, not just a page.  

1. **Flask `/score` route**  
   - Accepts: resume file + JD text (POST request)  
   - Runs extractor + analysis  
   - Returns JSON:  
     ```json
     {
       "fit_score": 78,
       "matched": ["python", "flask"],
       "missing": ["docker", "aws"],
       "weights": {...},
       "suggestions": ["Add docker experience in skills section"]
     }
     ```  

2. **Schemas with Pydantic**  
   - Define request + response models for clean structure  

3. **Unit tests**  
   - Create `tests/test_scoring.py`  
   - Use 2–3 sample resumes + JDs  
   - Assert Fit Score returns a number, matched/missing lists look correct  

✅ **Milestone:** You can `curl` or Postman the API and get JSON output.

---

## 🎨 Phase 4 — Frontend UI
**Goal:** React app for human-friendly interaction.  

1. **Setup React (Vite)**  
   - `npm create vite` → `frontend/`  
   - Install dependencies  

2. **Upload Form**  
   - File upload for resume  
   - Textarea for JD  

3. **API Call**  
   - On submit → send file + JD to Flask `/score`  
   - Receive JSON response  

4. **Results Panel**  
   - Show:  
     - Big Fit Score (0–100)  
     - Matched keywords (green chips)  
     - Missing keywords (red chips)  
     - Suggestions (bullets)  

✅ **Milestone:** Upload resume + JD → see live results in browser.

---

## 🔎 Phase 5 — Explainability & Polish
**Goal:** Make results transparent + user-friendly.  

1. **Weighted breakdown table**  
   - Show which required/preferred keywords affected the score  
2. **Reason strings**  
   - e.g., “Docker missing (−3)” or “Python matched (+3)”  
3. **Export options**  
   - Button to save results as JSON or Markdown file  
4. **Optional AI**  
   - Integrate OpenAI API toggle to rephrase missing keywords into bullet suggestions  

✅ **Milestone:** Results feel like a professional tool, not just raw output.

---

## 🚀 Phase 6 — Ship
**Goal:** Run easily + optionally deploy.  

1. **Run script**  
   - `run_local.sh` to launch backend + frontend together  
2. **README**  
   - Document setup, run steps, sample screenshots  
3. **Deployment (optional)**  
   - Deploy Flask + React to Render/Railway/Heroku  
   - Share demo link  

✅ **Milestone:** Resonance runs end-to-end, reproducible by anyone.

---

## 🌟 Stretch Goals (after MVP)
- Smarter synonyms with embeddings  
- Resume section detection (Education, Skills, Experience)  
- Batch scoring (one resume vs multiple JDs)  
- Role calibration profiles (weights differ for SWE vs Security vs AI)  
- Database for history + profiles  

---

## 📊 Progress Tracker
- ✅ Foundation (Phase 0)  
- 🔄 Currently: **Phase 1 (Text Extraction Engine)**  
- 🎯 Next Major Milestone: Fit Score via API  


