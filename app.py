import numpy as np
import re
import pickle
import nltk
import streamlit as st
import PyPDF2
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
import time
import json

load_dotenv()

# nltk.download('punkt')
# nltk.download('stopwords')

# Setting Gemini API key
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

# Load models
try:
    clf = pickle.load(open('clf.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please ensure 'clf.pkl' and 'tfidf.pkl' exist in the directory.")
    st.stop()

# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)  
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)  
    cleanText = re.sub(r'@\S+', '  ', cleanText)  
    cleanText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub(r'\s+', ' ', cleanText)  

    return cleanText

# Function to generate category and responsibilities
def generate_category(category, resume_text):
    prompt = f"""
    Resume Category: {category} \n\n
    Resume Text: {resume_text}\n\n
    Act like a highly skilled Resume Screening App with a deep understanding of various fields.
    Your task is to evaluate the given resume based on the resume category provided and determine if the resume matches the category. 
    If it matches, return the same category. If it doesn't match, provide the most appropriate category based on the resume content. No initials\n\n
    Additionally, suggest responsibilities and relevant skills required for that specific category based on industry standards. \n\n
    the response should be in a json format with the keys "Category", "Responsibilities" and "Skills"
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return "Error generating category after multiple attempts."



# Web app
def main():
    st.title("Resume Screening App")

    st.markdown("""
    **Welcome to the Resume Screening App!**  
    This app helps you automatically categorize resumes and provides a list of responsibilities and skills relevant to the category.
    
    Feel free to try it out by uploading a resume file below.
    """)

    upload_file = st.file_uploader('Upload Resume', type=['pdf', 'txt'])

    if upload_file is not None:
        try:
            if upload_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(upload_file)
                resume_text = "".join([page.extract_text() for page in pdf_reader.pages])
            else:
                resume_bytes = upload_file.read()
                resume_text = resume_bytes.decode('utf-8')

        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_features = tfidf.transform([cleaned_resume])  
        prediction_id = clf.predict(input_features)[0]

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer", 23: "Testing", 8: "DevOps Engineer", 20: "Python Developer",
            24: "Web Designing", 12: "HR", 13: "Hadoop", 3: "Blockchain", 10: "ETL Developer",
            18: "Operations Manager", 6: "Data Science", 22: "Sales", 16: "Mechanical Engineer",
            1: "Arts", 7: "Database", 11: "Electrical Engineering", 14: "Health and fitness",
            19: "PMO", 4: "Business Analyst", 9: "DotNet Developer", 2: "Automation Testing",
            17: "Network Security Engineer", 21: "SAP Developer", 5: "Civil Engineer", 0: "Advocate"
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        # Call  function to generate category and responsibilities
        response = generate_category(category_name, cleaned_resume)
        
        # Clean up the response (remove ```json and other irregularities)
        cleaned_response = re.sub(r'```json|```', '', response).strip()

        try:
            response_json = json.loads(cleaned_response)

            # Display the generated category
            st.subheader("Category of resume/CV:")
            st.write(response_json.get("Category", "N/A"))
            
            # Display responsibilities
            responsibilities = response_json.get("Responsibilities", [])
            if responsibilities:
                st.subheader("Responsibilities expected of this Category:")
                for responsibility in responsibilities:
                    st.write("- ", responsibility)
            else:
                st.write("No responsibilities found.")
            
            # Display relevant skills
            skills = response_json.get("Skills", [])
            if skills:
                st.subheader("Relevant Skills required for this Category:")
                for skill in skills:
                    st.write("- ", skill)
            else:
                st.write("No relevant skills found.")

        except json.JSONDecodeError as e:
            st.error("An error occurred, Please try again!")


if __name__ == "__main__":
    main()
