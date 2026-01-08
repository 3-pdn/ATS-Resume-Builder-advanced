# generate_samples.py - generate synthetic resumes and job descriptions for demo
import pandas as pd
import random
import os

os.makedirs('job_descriptions', exist_ok=True)
jd1 = '''Data Scientist
We are looking for a Data Scientist with 3+ years experience in Python, machine learning, SQL, and statistics.
Responsibilities: build models, analyze data, deploy ML pipelines.
Required skills: Python, Pandas, scikit-learn, SQL, machine learning, statistics.'''
jd2 = '''Software Engineer
Seeking Software Engineer with experience in Java, Spring, REST APIs, microservices, and cloud.
Required skills: Java, Spring Boot, REST, Docker, AWS.'''

with open('job_descriptions/data_scientist.txt','w') as f:
    f.write(jd1)
with open('job_descriptions/software_engineer.txt','w') as f:
    f.write(jd2)

# Create synthetic resumes (text) with labels (1=match for data scientist JD, 0=not)
names = ['Alex','Priya','Rohan','Sara','John','Maya','Vikram','Li','Chen','Aisha']
skills_ds = ['Python','Pandas','scikit-learn','SQL','statistics','machine learning','TensorFlow','PyTorch','data visualization']
skills_se = ['Java','Spring','REST','Docker','Kubernetes','AWS','microservices','Hibernate']

resumes = []
for i in range(200):
    name = random.choice(names)
    yrs = random.randint(0,10)
    if random.random() < 0.6:
        # make it closer to data scientist
        skills = random.sample(skills_ds, k=random.randint(3,6))
        extra = random.sample(skills_se, k=random.randint(0,2))
        label = 1
    else:
        skills = random.sample(skills_se, k=random.randint(2,5))
        extra = random.sample(skills_ds, k=random.randint(0,2))
        label = 0
    skills_all = skills + extra
    txt = f"""{name} - Resume
Summary:
Experienced professional with {yrs} years of experience working on projects.

Skills:
{', '.join(skills_all)}

Experience:
Worked on multiple projects using {skills_all[0]}. Built systems and collaborated with cross-functional teams.

Education:
B.Tech / B.Sc in relevant field.
"""
    resumes.append({'id': i, 'name': name, 'years_experience': yrs, 'text': txt, 'label': label})

df = pd.DataFrame(resumes)
df.to_csv('data/sample_resumes.csv', index=False)
print('Wrote data/sample_resumes.csv and job descriptions to job_descriptions/')