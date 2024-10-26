import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# This is a simplified list. In a real-world scenario, you'd want a more comprehensive list.
SKILLS = [
    "Python", "JavaScript", "Java", "C++", "C#", "Ruby", "PHP", "Swift", "Kotlin", "Go",
    "React", "Angular", "Vue.js", "Node.js", "Django", "Flask", "Spring", "ASP.NET",
    "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision",
    "Data Analysis", "Data Science", "Big Data", "Cloud Computing", "DevOps", "Agile",
    "SQL", "NoSQL", "MongoDB", "PostgreSQL", "MySQL", "Oracle", "Git", "Docker", "Kubernetes"
]

matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(text) for text in SKILLS]
matcher.add("SkillsMatcher", patterns)

def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    skills = set([doc[start:end].text.lower() for _, start, end in matches])
    return skills

