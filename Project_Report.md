A MINI PROJECT REPORT ON
“IntelliMatch: AI-Powered Resume Screening System”

SUBMITTED TO THE SAVITRIBAI PHULE PUNE UNIVERSITY, PUNE
IN THE PARTIAL FULFILLMENT OF THE REQUIREMENTS
FOR THE AWARD OF THE DEGREE OF

BACHELOR OF ENGINEERING IN COMPUTER ENGINEERING

BY

MR. GAURAV CHAVAN (TCOD68)
MR. VIVEK JADHAV (TCOD69)
MR. SUJAL KALAMKAR (TCOD65)

UNDER THE GUIDANCE OF
PROF. VIPUL GUNJAL

MINI PROJECT SUBMITTED TO
DEPARTMENT OF COMPUTER ENGINEERING

Dr. D. Y. PATIL UNITECH SOCIETY’S
DR. D. Y. PATIL INSTITUTE OF TECHNOLOGY, PIMPRI, PUNE-411018
(AFFILIATED TO SAVITRIBAI PHULE PUNE UNIVERSITY, PUNE)
(2025–2026)

---

DR. D. Y. PATIL UNITECH SOCIETY’S
DR. D. Y. PATIL INSTITUTE OF TECHNOLOGY, PUNE
DEPARTMENT OF COMPUTER ENGINEERING

CERTIFICATE

This is to certify that Mr. Aditya Anil Kulkarni and Mr. Pranit Hemant Pawar from Third Year Computer Engineering have successfully completed the Mini Project titled "IntelliMatch: AI-Powered Resume Screening System" in partial fulfillment of the Bachelor’s Degree in Computer Engineering as prescribed by Savitribai Phule Pune University for the academic year 2025–2026.

Prof. Vipul Gunjal 
Project Guide 

Dr. Chaya Jadhav
Head of Department

Dr. Nitin P. Sherje
Principal

Date: 
Place:

---

# Acknowledgement

We express our sincere gratitude to Prof. Vipul Gunjal, Project Guide, Department of Computer Engineering, for his valuable guidance, continuous encouragement, and constructive suggestions throughout the development of the mini project titled "IntelliMatch: AI-Powered Resume Screening System". His technical support and timely advice helped in understanding important concepts related to Natural Language Processing (NLP), text mining, and web application development.

We would also like to thank the Department of Computer Engineering, Dr. D. Y. Patil Institute of Technology, Pimpri, Pune, for providing the required academic environment and resources necessary for the successful completion of this project.

We are grateful to all faculty members of the department for their valuable inputs during different stages of the project. Finally, we would like to express our sincere thanks to our family and friends for their constant motivation and support during the execution and documentation of this mini project.

---

# Abstract

"IntelliMatch: AI-Powered Resume Screening System" is an intelligent web application developed to automate the process of filtering and evaluating candidate resumes against specific job descriptions. The project focuses on applying Natural Language Processing (NLP) techniques to analyze document contents (PDF or TXT) and score candidates based on their relevance to a target job role.

The system utilizes predefined keyword sets for various job roles. Data cleaning and preprocessing techniques such as tokenization, stopword removal, and punctuation filtering are applied to extract meaningful text. A hybrid scoring algorithm is implemented, utilizing Regex-based multi-word skill extraction and TF-IDF (Term Frequency-Inverse Document Frequency) paired with Cosine Similarity to calculate a highly accurate candidate match percentage.

The analytical engine is integrated with a modern, responsive Streamlit-based web application that allows recruiters to upload resumes, select job roles, and view detailed analysis results, including a breakdown of matched and missing skills. Furthermore, the system automatically logs all analysis history into a CSV dataset for future tracking.

This project demonstrates the seamless integration of machine learning NLP text processing, modern frontend web development, and file management systems into a complete, automated Applicant Tracking System (ATS) workflow.

---

# INDEX

Acknowledgement 
Abstract 
1. Introduction 
2. Problem Statement and Objectives 
3. System Methodology and Implementation 
4. Tools and Technology Used 
5. Results and Discussion 
6. Conclusion 
References 

---

# Chapter 1: Introduction

Resume screening is a critical application of Natural Language Processing (NLP) that focuses on identifying the relevance and qualifications of a candidate based on textual data in their resume. It is widely used in Human Resources (HR) and Applicant Tracking Systems (ATS) to streamline the recruitment process.

With the rapid growth of the job market, hundreds of resumes are submitted for a single job opening. Analyzing this data manually is difficult, time-consuming, and prone to human bias. Therefore, automated systems are required to process, extract, and evaluate such data efficiently.

The project titled "IntelliMatch: AI-Powered Resume Screening System" is developed to automatically parse candidate resumes and evaluate their fit for specific job roles using machine learning techniques. The system processes the uploaded document, performs text preprocessing, extracts key skills, and calculates a match score using a hybrid analytical algorithm.

The system uses TF-IDF (Term Frequency-Inverse Document Frequency) combined with direct skill mapping for feature extraction and similarity scoring. These techniques are highly efficient and widely used for text comparison tasks.

The project also features a beautiful, glassmorphism-styled web interface developed using Streamlit and custom CSS. Users can upload files, select roles, and instantly view visual sentiment results regarding the candidate's fit. A CSV-based data logging mechanism is used to store prediction history.

The main stages involved in the system are:
• Document Parsing and Text Extraction
• Text Cleaning and Preprocessing
• Skill Extraction (Pattern Matching)
• Similarity Scoring (TF-IDF & Cosine Similarity)
• Web Application Deployment & Data Logging

---

# Chapter 2: Problem Statement and Objectives

In the modern corporate world, HR departments and recruiters receive an overwhelming volume of resumes daily. Reviewing each document manually to verify if a candidate possesses the required skills is an inefficient bottleneck. It often leads to delayed hiring processes and the potential oversight of qualified candidates.

The problem addressed in this project is to develop an automated system that can analyze unstructured textual data from resumes and accurately match it against job requirements. The system should be capable of extracting raw text from PDFs, cleaning the noise, identifying relevant multi-word skills, and generating a reliable matching score.

The dataset used for this project consists of user-uploaded PDF and TXT resumes. Since raw document text contains noise, special characters, and varied formatting, robust preprocessing is required before feeding it into the scoring algorithm.

The objectives of the project are as follows:
• To extract raw text accurately from different file formats (PDF, TXT).
• To perform data cleaning and NLP preprocessing on unstructured text.
• To implement regex-based matching to extract complex, multi-word skills.
• To convert textual data into numerical vectors using TF-IDF and calculate Cosine Similarity.
• To build a hybrid scoring algorithm that accurately reflects candidate suitability.
• To develop a highly intuitive, premium-looking web interface using Streamlit.
• To automatically store all screening analysis history in a CSV file for record-keeping.

---

# Chapter 3: System Methodology and Implementation

The IntelliMatch project follows a structured NLP and software development workflow that includes multiple stages such as document parsing, preprocessing, feature extraction, evaluation, and deployment.

**DOCUMENT PARSING**
The system uses the `PyPDF2` library to read uploaded PDF files in binary mode, extracting text page by page. For TXT files, standard UTF-8 decoding is used.

**TEXT PREPROCESSING**
Raw text contains unnecessary elements such as formatting artifacts and punctuation marks. Preprocessing steps include converting text to lowercase, removing punctuation using regular expressions, tokenizing the text, and removing English stopwords using the `NLTK` library.

**SKILL EXTRACTION**
Unlike simple word-matching, the system employs Regex (Regular Expressions) to perform contextual skill extraction. It cleans skill keywords and searches for exact boundary matches within the raw text, successfully capturing multi-word skills like "machine learning" or "data analysis" despite spacing or punctuation differences.

**SCORING ALGORITHM**
The system uses a hybrid mathematical approach:
1. **Skill Match Score (70% Weight)**: The ratio of matched skills to total required skills.
2. **Contextual Similarity (30% Weight)**: TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert both the resume text and the job description into numerical vectors. `cosine_similarity` from `scikit-learn` is then calculated to measure the semantic closeness of the two documents.

These two metrics are combined to generate a final percentage score, capped at 100%.

**SYSTEM ARCHITECTURE**
The system architecture consists of multiple components working together:

User Uploads Resume → Streamlit Frontend → Backend Text Parsing → NLP Preprocessing → Hybrid Similarity Scoring → CSV Storage → Streamlit Results Dashboard

The frontend collects the user's file and job selection, the backend applies the NLP logic, the results are saved to `analysis_history.csv`, and the visual breakdown is rendered back to the user.

---

# Chapter 4: Tools and Technology Used

The development of the IntelliMatch project requires the integration of multiple tools and technologies.

• **Python**: Used as the primary programming language for implementing NLP logic and backend operations.
• **Streamlit**: Used as the frontend framework to create a highly responsive, interactive, and beautifully styled web application.
• **NLTK (Natural Language Toolkit)**: Used for text preprocessing tasks such as tokenization and stopword removal.
• **Scikit-learn**: Used for implementing TF-IDF vectorization and Cosine Similarity calculations.
• **PyPDF2**: Used for parsing and extracting raw text from PDF documents.
• **Regular Expressions (Regex)**: Used for advanced pattern matching and precise skill extraction.
• **CSV Module**: Used as a lightweight database to store historical analysis data.
• **HTML & Custom CSS**: Injected into the Streamlit app to design a premium "glassmorphism" interface and improve user experience.

---

# Chapter 5: Results and Discussion

The developed system was tested using various sample resumes to verify its parsing functionality and scoring accuracy.

The application provides an intuitive upload interface. Users can seamlessly upload a PDF or TXT file and select a target job role from a dropdown menu. 

Upon clicking the Analyze button, the system processes the document and generates a visual dashboard. The prediction results are displayed on the screen with dynamic metric cards. 
- A high score categorizes the candidate as an "Excellent Fit" or "Good Fit".
- A low score triggers a "Moderate Fit" or "Poor Fit" warning.

A major feature of the results page is the **Skill Breakdown** section. The system transparently displays which key requirements the candidate met and which ones were missing, allowing recruiters to make quick, informed decisions.

Furthermore, the system maintains a history of all predictions in the `analysis_history.csv` file, logging the Date, Filename, Role, Score, Status, and extracted skills.

The system successfully solves the problem of multi-word skill matching and provides a much more reliable similarity score than standard TF-IDF alone.

---

# Chapter 6: Conclusion

The "IntelliMatch: AI-Powered Resume Screening System" successfully demonstrates the use of Natural Language Processing techniques for document classification and candidate evaluation.

The system integrates text parsing, NLP preprocessing, feature extraction, similarity scoring, and web deployment into a single, cohesive application. It provides a highly premium and user-friendly interface for performing ATS tasks.

The project helps in understanding the practical implementation of text mining concepts, regex pattern matching, and mathematical similarity algorithms. The integration of Streamlit and CSV logging enhances the usability of the system by enabling real-time evaluations and record tracking.

Future improvements may include integrating Large Language Models (LLMs) like OpenAI or Gemini for deeper semantic understanding, adding support for DOCX files, and implementing a centralized database like PostgreSQL or MongoDB for enterprise-scale data management.

---

# References

• Scikit-learn Documentation (TF-IDF & Cosine Similarity)
• Streamlit Documentation (Web Framework & UI)
• NLTK Documentation (Natural Language Toolkit)
• PyPDF2 Documentation (PDF Parsing)
• Python Regular Expressions (re) Module Documentation
• Concept of Applicant Tracking Systems (ATS) and Resume Parsing techniques.
