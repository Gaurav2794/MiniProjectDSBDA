import re
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import os
import csv
from datetime import datetime

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

JOB_ROLES = {
    "Data Analyst": ["python", "sql", "excel", "pandas", "data analysis", "visualization", "statistics", "tableau", "power bi"],
    "Software Engineer": ["java", "c++", "python", "algorithms", "data structures", "git", "docker", "aws"],
    "Web Developer": ["html", "css", "javascript", "react", "angular", "node js", "mongodb", "typescript"],
    "Machine Learning Engineer": ["python", "tensorflow", "pytorch", "scikit learn", "numpy", "pandas", "deep learning", "nlp"],
    "DevOps Engineer": ["docker", "kubernetes", "jenkins", "aws", "terraform", "ansible", "linux", "ci/cd"]
}

stop_words = set(stopwords.words('english'))

def get_available_job_roles():
    "Get list of available job roles."
    return list(JOB_ROLES.keys())

def extract_text(file_path):
    "Extract text from PDF or TXT file."
    if file_path.lower().endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + '\n'
            return text
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format. Use PDF or TXT.")

def preprocess_text(text):
    "Clean and preprocess text."
    text = text.lower()
    text = re.sub(r'[' + re.escape(string.punctuation) + r']', ' ', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if len(word) > 1 and word not in stop_words]
    return ' '.join(tokens)

def get_job_keywords(job_role):
    "Get keywords for job role."
    if job_role in JOB_ROLES:
        return JOB_ROLES[job_role]
    return []

def extract_skills(resume_text, job_keywords):
    "Extract matching skills from resume."
    matching_skills = []
    resume_text_lower = resume_text.lower()
    for skill in job_keywords:
        skill_clean = skill.replace(' ', r'[\s\W]+')
        if re.search(r'\b' + skill_clean + r'\b', resume_text_lower):
            matching_skills.append(skill)
        elif skill in resume_text_lower: # fallback
             matching_skills.append(skill)
    return list(dict.fromkeys(matching_skills))

def calculate_similarity(resume_text, job_keywords, matched_skills):
    "Calculate similarity based on skill match and TF-IDF."
    if not job_keywords:
        return 0.0
    
    # 1. Skill Match Percentage (Weight: 70%)
    skill_score = len(matched_skills) / len(job_keywords)
    
    # 2. Contextual Similarity (Weight: 30%)
    job_text = ' '.join(job_keywords)
    documents = [resume_text, job_text]
    try:
        tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
        tfidf_matrix = tfidf.fit_transform(documents)
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    except Exception:
        cosine_sim = 0.0
        
    final_score = (skill_score * 0.7) + (cosine_sim * 0.3)
    return min(final_score, 1.0)

def get_recommendation(score):
    "Get recommendation based on score."
    if score >= 0.70:
        return "Excellent Fit", "Candidate has a strong match with the required skills."
    elif score >= 0.40:
        return "Good Fit", "Candidate has many of the key skills, but some are missing."
    elif score >= 0.20:
        return "Moderate Fit", "Candidate shows some potential but lacks several core skills."
    else:
        return "Poor Fit", "Candidate is missing most of the required skills for this role."

def save_analysis(filename, role, score_percent, status, matched_skills, missing_skills):
    "Save the analysis result to a CSV file."
    file_exists = os.path.isfile('analysis_history.csv')
    with open('analysis_history.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Resume Filename', 'Role', 'Score', 'Status', 'Matched Skills', 'Missing Skills'])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            filename,
            role,
            f"{score_percent:.1f}%",
            status,
            ", ".join(matched_skills),
            ", ".join(missing_skills)
        ])

