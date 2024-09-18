Resume Screening App
Welcome to the Resume Screening App, a machine learning-powered tool designed to automatically categorize resumes and provide the relevant responsibilities and skills associated with the detected job role. This app is built using Python, Streamlit, and various machine learning libraries.

Features
Upload resumes in PDF or text format.
Automatic resume text cleaning and pre-processing.
Predicts the job category based on resume content.
Provides a list of expected responsibilities and relevant skills for the predicted category.
Utilizes Gemini API for additional resume insights.
How to Use
Upload a Resume: Upload a resume file in either PDF or text format.

Category Prediction: The app will process the resume, predict its job category, and display it.

Responsibilities and Skills: You will receive a list of responsibilities and relevant skills associated with the predicted category.

Installation
Prerequisites
Python 3.8 or above
pip package manager
Dependencies
Install the required packages using the following command:

bash
Copy code
pip install -r requirements.txt
Contents of requirements.txt:

Copy code
numpy
nltk
PyPDF2
streamlit
google-generativeai
python-dotenv
scikit-learn
Run the App
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/resume-screening-app.git
Navigate into the directory:

bash
Copy code
cd resume-screening-app
Make sure to set up your environment variables in a .env file. You will need an API key for Google Gemini:

makefile
Copy code
API_KEY=your_gemini_api_key
Run the app using Streamlit:

bash
Copy code
streamlit run app.py
Open your browser and navigate to the URL provided by Streamlit, typically http://localhost:8501.

Folder Structure
bash
Copy code
resume-screening-app/
│
├── clf.pkl                   # Pre-trained classifier model (machine learning)
├── tfidf.pkl                 # TF-IDF vectorizer model
├── app.py                    # Main Streamlit application script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .env                      # Environment variables (API key for Gemini)
└── data/                     # Folder for sample resumes (optional)
How it Works
Text Preprocessing: The app cleans resume text by removing URLs, special characters, and unnecessary spaces.

Prediction Model: A machine learning classifier predicts the job category based on the text content of the resume. The model is pre-trained using TF-IDF vectorization.

Responsibilities & Skills: The app calls the Gemini API to generate a JSON response, which includes:

Predicted job category
Relevant responsibilities
Relevant skills
Results Display: The app displays the predicted category, responsibilities, and relevant skills directly in the Streamlit interface.

Tech Stack
Backend: Python, scikit-learn, Google Gemini API
Frontend: Streamlit
Text Processing: NLTK
Machine Learning: TF-IDF, Pre-trained Classifier
Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Fork the repository (https://github.com/pfrimpong11/resume-screening-app.git)
Create a feature branch (git checkout -b feature/your-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/your-feature)
Create a new Pull Request
