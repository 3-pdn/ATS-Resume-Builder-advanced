# ats_scoring.py - compute ATS score and suggestions based on keyword coverage
from parser import parse_text
import re

def score_resume_against_jd(resume_text: str, jd_text: str) -> dict:
    res = parse_text(resume_text)
    jd = jd_text.lower()
    # JD required skills — extract words after 'Required skills:' or use COMMON_SKILLS intersection
    req_skills = []
    m = re.search(r'required skills?:\s*(.*)', jd)
    if m:
        req_skills = [s.strip() for s in re.split('[,;]| and ', m.group(1))]
        req_skills = [s.lower() for s in req_skills if s.strip()]
    # fallback: take words from jd that match skills in parsed resume
    if not req_skills:
        req_skills = res['skills']
    matched = [s for s in res['skills'] if any(s in r for r in req_skills)]
    skill_score = len(matched) / max(1, len(req_skills))
    # experience score
    yrs_needed = 0
    m2 = re.search(r'(\d+)\+?\s+years', jd)
    if m2:
        yrs_needed = int(m2.group(1))
    exp_score = 1.0 if (res['years_experience'] or 0) >= yrs_needed else ( (res['years_experience'] or 0) / max(1, yrs_needed) if yrs_needed>0 else 1.0)
    # education score simple
    edu_score = 1.0 if res['education'] else 0.5
    # final weighted score
    total = 0.6*skill_score + 0.3*exp_score + 0.1*edu_score
    suggestions = []
    # suggest missing skills
    missing = [s for s in req_skills if not any(s in ms for ms in res['skills'])]
    if missing:
        suggestions.append('Consider adding or emphasizing these skills: ' + ', '.join(missing))
    if (res['years_experience'] or 0) < yrs_needed:
        suggestions.append(f'Consider highlighting relevant experience — JD asks for {yrs_needed} years.')
    return {
        'score': round(float(total)*100,2),
        'skill_coverage': round(skill_score*100,2),
        'experience_score': round(exp_score*100,2),
        'education_score': round(edu_score*100,2),
        'matched_skills': matched,
        'missing_skills': missing,
        'suggestions': suggestions
    }

if __name__ == '__main__':
    jd = open('job_descriptions/data_scientist.txt').read()
    res = open('data/sample_resumes.csv').read().splitlines()[1]
    print(score_resume_against_jd(res, jd))