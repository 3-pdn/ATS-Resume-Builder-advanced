# ATS Resume Builder — Advanced Project

This project provides an Applicant Tracking System (ATS) friendly resume builder and scorer.
It includes:
- Resume parsing utilities
- Rule-based ATS scoring and keyword-matching
- Optional training script to build a simple classifier (TF-IDF + Logistic Regression)
- Streamlit app to paste/upload a resume, view parsed fields and get an ATS score & suggestions
- Sample resumes (text) and job description examples

## Contents
- data/sample_resumes.csv        : synthetic labeled resumes (text + label)
- job_descriptions/              : example JD files (txt)
- parser.py                      : resume parsing utilities
- ats_scoring.py                 : rule-based scorer & suggestions
- train_model.py                 : optional TF-IDF + LR training script
- app_streamlit.py               : Streamlit app for interactive scoring
- generate_samples.py            : script that created the synthetic resumes (for reproducibility)
- requirements.txt
- README.md

## How to run
1. Create virtual environment:
   python -m venv .venv
   source .venv/bin/activate    # mac/linux
   .venv\Scripts\activate     # windows

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app_streamlit.py

4. (Optional) Train the ML model:
   python train_model.py

Notes:
- The scoring is primarily rule-based (keyword match, experience years, education). The ML script is optional and demonstrates how to train a classifier if you provide labeled data.
- Replace sample job descriptions with your target JD for more accurate scoring.
