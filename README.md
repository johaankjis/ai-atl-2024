# AI ATL Hackathon 2024 - Resume Matcher Application

## Overview

This is a Resume Matcher web application built for the AI ATL Hackathon 2024. The application uses Natural Language Processing (NLP) and Machine Learning to analyze resumes against job descriptions, providing match percentages and actionable feedback to help job seekers improve their applications.

## Project Architecture

### Core Components

1. **Flask Web Application (`app.py`)**
   - Main entry point for the web application
   - Handles HTTP requests and routing
   - Integrates Google's Gemini Pro AI model for content generation
   - Provides endpoints for resume matching and feedback generation

2. **Resume Matcher (`resume_matcher.py`)**
   - Core matching algorithm using TF-IDF vectorization and cosine similarity
   - Text preprocessing with spaCy for NLP operations
   - Skill-based matching with weighted scoring (60% text similarity + 40% skill match)
   - Calculates overall match percentage between resume and job description

3. **Skills Extractor (`skills_extractor.py`)**
   - Uses spaCy's PhraseMatcher for pattern recognition
   - Maintains a comprehensive list of technical skills (programming languages, frameworks, methodologies)
   - Extracts relevant skills from both resumes and job descriptions
   - Identifies missing skills for improvement suggestions

4. **Database Module (`database.py`)**
   - SQLite database integration for storing job descriptions
   - Provides CRUD operations for job description management
   - Automatically initializes database schema on startup

### Frontend Components

- **Templates (`templates/`)**
  - `index.html`: Main input form for resume and job description
  - `result.html`: Results page displaying match percentage and feedback

- **Static Assets (`static/`)**
  - `styles.css`: Application styling with modern UI design
  - `script.js`: Client-side JavaScript for interactive elements (percentage circle visualization)

## Technologies Used

- **Backend**: Python 3, Flask
- **NLP**: spaCy (en_core_web_sm model)
- **Machine Learning**: scikit-learn (TF-IDF, cosine similarity)
- **AI Integration**: Google Generative AI (Gemini Pro)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 5.15.3

## Key Features

1. **Resume-to-Job Matching**: Calculates similarity score between resume and job description
2. **Skills Analysis**: Identifies matching skills and skills gaps
3. **Intelligent Feedback**: Provides actionable suggestions for resume improvement
4. **Modern UI**: Clean, responsive interface with visual percentage indicators
5. **Text Preprocessing**: Advanced NLP preprocessing including lemmatization and stop word removal

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/johaankjis/ai-atl-2024.git
   cd ai-atl-2024
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the spaCy English language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Configure Google Gemini API (if using AI features):
   - Replace `'GEMINI_API_KEY'` in `app.py` with your actual API key

### Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Enter your resume and job description in the provided text areas
4. Click "Match Resume" to see results

## How It Works

### Matching Algorithm

1. **Text Preprocessing**: 
   - Removes stop words and punctuation
   - Applies lemmatization to normalize word forms
   - Converts text to lowercase

2. **Similarity Calculation**:
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
   - Computes cosine similarity between resume and job description vectors

3. **Skills Extraction**:
   - Pattern matching against predefined skills database
   - Identifies technical skills, frameworks, and methodologies

4. **Score Calculation**:
   - Final score = (0.6 × text_similarity + 0.4 × skill_match) × 100
   - Provides balanced assessment of both content and specific skills

5. **Feedback Generation**:
   - Highlights matching skills to emphasize
   - Lists missing skills to develop or add
   - Provides actionable improvement suggestions

## File Structure

```
ai-atl-2024/
├── app.py                  # Main Flask application
├── resume_matcher.py       # Core matching logic
├── skills_extractor.py     # Skills extraction module
├── database.py             # Database operations
├── test_app.py            # Simple test application
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Results display
├── static/
│   ├── styles.css         # Application styles
│   └── script.js          # Client-side scripts
└── README.md              # This file
```

## AI ATL Hackathon 2024 Tracks

We participated in 2 tracks for AI ATL Hackathon 2024:

### Track 1: Get started with Google DeepMind's AI Developer Stack by Google Cloud

**Demo Video**: https://youtu.be/E9V6MhxHxPM

This track showcases the integration of Google's Gemini Pro model for AI-powered content generation and resume analysis.

### Track 2: AI Alignment - Evaluating LLMs

Presented by the AI safety initiative @ GT and proudly supported by Anthropic and Apart Research!

- **Final Document**: https://docs.google.com/document/d/1dyzEjGUQhtF19D2mYHxHzO6szpA8VTixdFi8uLbVsbs/edit?usp=sharing
- **Demo Video**: https://youtu.be/38gDCgoFKw8

## Future Enhancements

- PDF resume upload and parsing
- Advanced skill taxonomy and ontology
- Machine learning model for better matching
- User authentication and history tracking
- Integration with job boards APIs
- Multi-language support
- Resume improvement suggestions using Gemini AI

## Contributing

This project was created for the AI ATL Hackathon 2024. Contributions and suggestions are welcome!

## License

This project is available for educational and demonstration purposes.
