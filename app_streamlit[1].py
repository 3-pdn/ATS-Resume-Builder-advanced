# app_streamlit.py - Streamlit app for ATS resume scoring and suggestions
import streamlit as st
from ats_scoring import score_resume_against_jd
import os

st.set_page_config(page_title='ATS Resume Builder', layout='centered')
st.title('ATS Resume Builder & Scorer')

st.sidebar.header('Job Description')
jd_files = []
if os.path.exists('job_descriptions'):
    jd_files = [f for f in os.listdir('job_descriptions') if f.endswith('.txt')]
selected_jd = st.sidebar.selectbox('Choose Job Description', options=['--sample--'] + jd_files)

if selected_jd == '--sample--' and os.path.exists('job_descriptions/data_scientist.txt'):
    jd_text = open('job_descriptions/data_scientist.txt').read()
elif selected_jd and selected_jd != '--sample--':
    jd_text = open(os.path.join('job_descriptions', selected_jd)).read()
else:
    jd_text = st.sidebar.text_area('Paste job description here', height=200)

st.sidebar.subheader('Upload resume (txt or paste below)')
uploaded = st.file_uploader('Upload resume (txt)', type=['txt'])
resume_text = ''
if uploaded:
    resume_text = uploaded.read().decode('utf-8')
else:
    resume_text = st.text_area('Or paste resume text here', height=300)

if st.button('Score Resume'):
    if not resume_text.strip():
        st.error('Please upload or paste a resume.')
    else:
        result = score_resume_against_jd(resume_text, jd_text or '')
        st.metric('ATS Score', f"{result['score']} / 100")
        st.write('Skill coverage:', f"{result['skill_coverage']}%", '| Experience score:', f"{result['experience_score']}%", '| Education score:', f"{result['education_score']}%" )
        st.write('Matched skills:', result['matched_skills'])
        st.write('Missing skills:', result['missing_skills'])
        if result['suggestions']:
            st.subheader('Suggestions')
            for s in result['suggestions']:
                st.write('-', s)
        st.balloons()

st.info('Tip: Use the Job Description on the left or paste your target JD to get tailored suggestions.')
