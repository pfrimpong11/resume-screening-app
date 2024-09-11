import numpy
import re
import pickle
import nltk
import streamlit as st


# nltk.download('punkt')
# nltk.download('stopwords')

# Loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

# function to clean text
def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)  # Use raw string r'...'
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)  # Use raw string
    cleanText = re.sub(r'@\S+', '  ', cleanText)  # Use raw string
    cleanText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub(r'\s+', ' ', cleanText)  # Use raw string

    return cleanText

# web app
def main():
    st.title("Resume Screening App")
    upload_file = st.file_uploader('Upload Resume', type=['pdf', 'txt'])

    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode('utf-8')

        except UnicodeDecodeError:
            # if utf-8 decoding fails, try decoding with latin-1
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_features = tfidf.transform([cleaned_resume])  # Pass as a list
        prediction_id = clf.predict(input_features)[0]
        st.write(f'Predicted ID: {prediction_id}')

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        st.write("Predicted Category:", category_name)



# python main
if __name__ == "__main__":
    main()
