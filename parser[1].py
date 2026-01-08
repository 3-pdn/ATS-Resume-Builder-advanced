# parser.py - simple resume parser that extracts skills, years of experience, education
import re
from typing import Dict, List

COMMON_SKILLS = ['python','pandas','numpy','scikit-learn','tensorflow','pytorch','sql','docker','aws','java','spring','rest','kubernetes','machine learning','deep learning','statistics','nlp','spark']

def parse_text(text: str) -> Dict:
    txt = text.lower()
    # extract years of experience (simple)
    yrs = None
    m = re.search(r'(\d+)\+?\s+years', txt)
    if m:
        yrs = int(m.group(1))
    else:
        m2 = re.search(r'(\d+)\s+years', txt)
        if m2:
            yrs = int(m2.group(1))
    # extract skills by keyword matching
    found_skills = []
    for s in COMMON_SKILLS:
        if s in txt:
            found_skills.append(s)
    # extract education keywords
    education = []
    for ed in ['b.tech','bachelor','m.tech','master','phd','b.sc','b.a']:
        if ed in txt:
            education.append(ed)
    return {
        'years_experience': yrs,
        'skills': list(set(found_skills)),
        'education': education
    }

if __name__ == '__main__':
    sample = """Priya
    Summary: 4 years experience in Python, Pandas and Machine Learning.
    Skills: Python, Pandas, scikit-learn, SQL.
    Education: B.Tech in Computer Science."""
    print(parse_text(sample))