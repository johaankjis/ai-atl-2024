from flask import Flask, render_template, request
from resume_matcher import match_resume_to_job, suggest_improvements
from skills_extractor import extract_skills
import google.generativeai as genai

app = Flask(__name__)

# Configure the API with your key
# This step is crucial for authentication with Google's servers
genai.configure(api_key='AIzaSyCktDC2_dqfLh3GcrwGBh2XhkuQs9V1Lxg')

# Initialize the Gemini Pro model
# 'gemini-pro' is the model name for the text-only version
model = genai.GenerativeModel('gemini-pro')

def generate_content(prompt, max_tokens=None, temperature=0.7):
    """
    Generate content using the Gemini Pro model.
    
    Args:
    prompt (str): The input text to guide the model's generation.
    max_tokens (int, optional): The maximum number of tokens in the response.
    temperature (float, optional): Controls randomness in generation. Higher values (e.g., 1.0) 
                                   make output more random, while lower values (e.g., 0.2) 
                                   make it more deterministic.
    
    Returns:
    str: The generated text content.
    """
    try:
        # Generate content based on the prompt
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature
            )
        )
        
        # Check if the response contains text
        if response.text:
            return response.text
        else:
            return "No content generated."
    
    except Exception as e:
        # Handle any errors that occur during generation
        return f"An error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.form['resume']
        job_description = request.form['job_description']
        
        match_percentage = match_resume_to_job(resume, job_description)
        print(f"Match percentage in app.py: {match_percentage}")  # Add this line
        missing_skills = suggest_improvements(resume, job_description)
        resume_skills = extract_skills(resume)
        job_skills = extract_skills(job_description)
        
        feedback = generate_feedback(resume_skills, job_skills, missing_skills)
        
        return render_template('result.html', 
                               match_percentage=match_percentage, 
                               missing_skills=missing_skills,
                               feedback=feedback)
    
    return render_template('index.html')

def generate_feedback(resume_skills, job_skills, missing_skills):
    feedback = []
    
    # Suggest highlighting matching skills
    matching_skills = resume_skills.intersection(job_skills)
    if matching_skills:
        feedback.append("Skills that match the job description:")
        feedback.extend([f"- {skill}" for skill in matching_skills])
    
    # Suggest adding missing skills
    if missing_skills:
        feedback.append("\nConsider adding or developing these skills:")
        feedback.extend([f"- {skill}" for skill in missing_skills])
    
    return "\n".join(feedback)

if __name__ == '__main__':
    print("Starting the Resume Matcher application...")
    print("Open your web browser and navigate to http://127.0.0.1:5000")
    app.run(debug=True)
