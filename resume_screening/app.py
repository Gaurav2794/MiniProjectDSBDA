import streamlit as st
from utils import (
    extract_text, preprocess_text, get_job_keywords, get_available_job_roles,
    calculate_similarity, extract_skills, get_recommendation, save_analysis
)
import os

st.set_page_config(page_title="Resume Screening System", layout="wide")

# Custom CSS for premium UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Global Text Colors */
    .stApp p, .stApp div, .stApp span, .stApp label {
        color: #f8fafc;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-weight: 700 !important;
    }
    
    /* Header background removal */
    .stApp > header {
        background-color: transparent !important;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #10b981 !important;
        text-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
        background: linear-gradient(90deg, #60a5fa 0%, #3b82f6 100%);
    }
    
    /* Upload area */
    .stFileUploader > div > div {
        background-color: rgba(30, 41, 59, 0.5);
        border: 2px dashed #475569;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    .stFileUploader > div > div:hover {
        border-color: #38bdf8;
        background-color: rgba(56, 189, 248, 0.05);
    }
    
    /* Custom container */
    .glass-container {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid #10b981;
        color: #34d399 !important;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 6px;
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    .missing-tag {
        display: inline-block;
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid #ef4444;
        color: #f87171 !important;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 6px;
        font-size: 0.95rem;
        font-weight: 500;
    }

    /* Subheaders inside containers */
    .section-title {
        color: #38bdf8;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        border-bottom: 1px solid rgba(56, 189, 248, 0.2);
        padding-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 2rem 0 3rem 0;'>
    <h1 style='font-size: 4rem; margin-bottom: 0.5rem; background: -webkit-linear-gradient(45deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>AI Resume Screener</h1>
    <p style='font-size: 1.3rem; color: #94a3b8;'>Intelligent parsing, accurate matching, and beautiful analysis</p>
</div>
""", unsafe_allow_html=True)

job_roles = get_available_job_roles()

st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='section-title'>Upload Candidate Resume</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=['pdf', 'txt'], help="Supported formats: PDF, TXT")

with col2:
    st.markdown("<div class='section-title'>Target Job Role</div>", unsafe_allow_html=True)
    job_role = st.selectbox("", job_roles, index=0, help="Select the role to match the candidate against")

st.markdown("</div>", unsafe_allow_html=True)

# Wrap button in columns to control width
btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
with btn_col2:
    analyze_btn = st.button("Analyze Candidate Match", use_container_width=True)

if analyze_btn:
    if uploaded_file and job_role:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            with st.spinner("Analyzing and matching skills..."):
                raw_text = extract_text(temp_path)
                processed_text = preprocess_text(raw_text)
                job_keywords = get_job_keywords(job_role)
                
                # Extract skills from raw text for better matching capability
                skills_found = extract_skills(raw_text, job_keywords) 
                
                similarity_score = calculate_similarity(processed_text, job_keywords, skills_found)
                score_percent = similarity_score * 100
                status, message = get_recommendation(similarity_score)
                
                missing_skills = [s for s in job_keywords if s not in skills_found]
                # Save the results to CSV
                save_analysis(uploaded_file.name, job_role, score_percent, status, skills_found, missing_skills)

            st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
            st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
            st.markdown("<div class='section-title'>Analysis Results</div>", unsafe_allow_html=True)
            
            res_col1, res_col2 = st.columns([1, 2])
            
            with res_col1:
                st.metric("Match Score", f"{score_percent:.1f}%")
                
                if score_percent >= 70:
                    st.success(f"**{status}**\n\n{message}")
                elif score_percent >= 40:
                    st.info(f"**{status}**\n\n{message}")
                elif score_percent >= 20:
                    st.warning(f"**{status}**\n\n{message}")
                else:
                    st.error(f"**{status}**\n\n{message}")
                    
            with res_col2:
                st.markdown("### Skill Breakdown")
                
                st.markdown("**Matched Requirements**")
                if skills_found:
                    skills_html = "".join([f"<span class='skill-tag'>{s.title()}</span>" for s in skills_found])
                    st.markdown(skills_html, unsafe_allow_html=True)
                else:
                    st.markdown("<p style='color: #94a3b8; font-style: italic;'>No key skills from the job description matched.</p>", unsafe_allow_html=True)
                
                st.markdown("<br>**Missing Requirements**", unsafe_allow_html=True)
                if missing_skills:
                    missing_html = "".join([f"<span class='missing-tag'>{s.title()}</span>" for s in missing_skills])
                    st.markdown(missing_html, unsafe_allow_html=True)
                else:
                    st.markdown("<p style='color: #94a3b8; font-style: italic;'>All key skills are present! Excellent profile.</p>", unsafe_allow_html=True)
                    
            st.markdown("</div>", unsafe_allow_html=True)

            # Document preview
            with st.expander("View Parsed Document Text"):
                st.text_area("", raw_text, height=300)

        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    else:
        st.warning("Please upload a resume document before analyzing.")

