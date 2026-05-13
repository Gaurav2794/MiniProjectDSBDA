# AI-Based Resume Screening System

## Setup & Run

1. Install dependencies:
   ```
   cd resume_screening
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

3. Open browser to http://localhost:8501

## Test
- Upload `resumes/sample_resume.txt` or `sample_resume.pdf`
- Job role: "Data Analyst"
- Expected: ~80% match, skills like python/sql, Good Fit

## Features
- PDF/TXT support
- TF-IDF + Cosine Similarity
- Preprocessing (NLTK)
- Colored UI, progress bar

