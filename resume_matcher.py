import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills_extractor import extract_skills

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Remove stop words and punctuation, and lemmatize the remaining tokens
    return " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

def calculate_similarity(text1, text2):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    # Fit and transform the texts
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    print(f"Raw similarity score: {similarity}")
    return similarity

def match_resume_to_job(resume_text, job_description):
    print("Starting match_resume_to_job function")
    print(f"Resume length: {len(resume_text)}")
    print(f"Job description length: {len(job_description)}")

    # Preprocess both texts
    processed_resume = preprocess_text(resume_text)
    processed_job = preprocess_text(job_description)
    
    print(f"Processed resume length: {len(processed_resume)}")
    print(f"Processed job description length: {len(processed_job)}")

    # Calculate text similarity
    text_similarity = calculate_similarity(processed_resume, processed_job)
    print(f"Text similarity: {text_similarity}")
    
    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    
    print(f"Resume skills: {resume_skills}")
    print(f"Job skills: {job_skills}")

    # Calculate skill match
    matching_skills = resume_skills.intersection(job_skills)
    skill_match_percentage = len(matching_skills) / len(job_skills) if job_skills else 0
    print(f"Matching skills: {matching_skills}")
    print(f"Skill match percentage: {skill_match_percentage}")
    
    # Combine text similarity and skill match (you can adjust the weights)
    match_percentage = (0.6 * text_similarity + 0.4 * skill_match_percentage) * 100
    print(f"Final match percentage: {match_percentage}")
    
    return match_percentage

def suggest_improvements(resume_text, job_description):
    # Extract key skills from the job description
    job_skills = extract_skills(job_description)
    
    # Extract skills from the resume
    resume_skills = extract_skills(resume_text)
    
    # Find missing skills
    missing_skills = job_skills - resume_skills
    
    return list(missing_skills)

# Example usage
if __name__ == "__main__":
    resume = """
    Experienced software developer with expertise in Python, JavaScript, and machine learning.
    Proficient in developing web applications using Django and React.
    Strong problem-solving skills and ability to work in a team environment.
    """

    job_description = """
    We are looking for a skilled software developer with experience in Python and JavaScript.
    The ideal candidate should have knowledge of machine learning, React, and cloud computing.
    Strong communication skills and experience with Agile methodologies are required.
    """

    match_percentage = match_resume_to_job(resume, job_description)
    print(f"Resume match: {match_percentage:.2f}%")

    missing_skills = suggest_improvements(resume, job_description)
    print("Skills to improve:")
    for skill in missing_skills:
        print(f"- {skill}")
