# Resume Screening App

Welcome to the Resume Screening App, a machine learning-powered tool designed to automatically categorize resumes and provide relevant responsibilities and skills associated with the detected job role. This app is built using Python, Streamlit, and various machine learning libraries.

## Features
- **Upload Resumes**: Supports PDF or text format.
- **Text Cleaning**: Automatic resume text cleaning and pre-processing.
- **Job Category Prediction**: Predicts the job category based on resume content.
- **Responsibilities and Skills**: Provides a list of expected responsibilities and relevant skills for the predicted category.
- **Gemini API**: Utilizes Gemini API for additional resume insights.

## How to Use
1. **Upload a Resume**: Upload a resume file in either PDF or text format.
2. **Category Prediction**: The app will process the resume, predict its job category, and display it.
3. **Responsibilities and Skills**: You will receive a list of responsibilities and relevant skills associated with the predicted category.

## Installation

### Prerequisites
- Python 3.8 or above
- pip package manager

### Dependencies
Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Run the App
1. Clone this repository:
```bash
git clone https://github.com/pfrimpong11/resume-screening-app.git
```

2. Navigate into the directory:
```bash
cd resume-screening-app
```

3. Set up your environment variables in a .env file. You will need an API key for Google Gemini:
Contents of .env:
```makefile
API_KEY=your_gemini_api_key
```

4. Run the app using Streamlit:
```bash
streamlit run app.py
```

5. Open your browser and navigate to the URL provided by Streamlit, typically http://localhost:8501

# Folder Structure
```bash
resume-screening-app/
│
├── clf.pkl                   # Pre-trained classifier model (machine learning)
├── tfidf.pkl                 # TF-IDF vectorizer model
├── app.py                    # Main Streamlit application script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .env                      # Environment variables (API key for Gemini)
└── data/                     # Folder for sample resumes (optional)
```

## How it Works
1. Text Preprocessing: The app cleans resume text by removing URLs, special characters, and unnecessary spaces.
2. Prediction Model: A machine learning classifier predicts the job category based on the text content of the resume. The model is pre-trained using TF-IDF vectorization.
3. Responsibilities & Skills: The app calls the Gemini API to generate a JSON response, which includes:
- Predicted job category
- Relevant responsibilities
- Relevant skills
4. Results Display: The app displays the predicted category, responsibilities, and relevant skills directly in the Streamlit interface.

## Tech Stack
- Backend: Python, scikit-learn, Google Gemini API
- Frontend: Streamlit
- Text Processing: NLTK
- Machine Learning: TF-IDF, Pre-trained Classifier

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
1.
```bash
Fork the repository (https://github.com/pfrimpong11/resume-screening-app.git)
```
2. Create a feature branch:
```bash
git checkout -b feature/your-feature
```
3. Commit your changes:
```bash
git commit -am 'Add new feature'
```
4. Push to the branch:
```bash
git push origin feature/your-feature
```
5. Create a new Pull Request
