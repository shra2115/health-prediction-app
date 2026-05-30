# 🏥 Health Prediction Application

## 📌 Project Overview

The Health Prediction Application is an AI-powered healthcare solution developed using Python, Streamlit, SQLite, and Machine Learning.

The application enables users to manage patient records and predict potential health risks using blood test parameters such as Glucose, Haemoglobin, and Cholesterol. The predicted health condition is automatically generated and stored in the Remarks field.

This project demonstrates CRUD operations, data validation, database management, machine learning integration, and user-friendly application development.

---

## 🎯 Objectives

* Store and manage patient health records.
* Validate patient information before processing.
* Predict possible health risks using machine learning.
* Provide a simple and interactive user interface.
* Demonstrate AI/ML integration within a healthcare application.

---

## ✨ Features

### Patient Management

* Add new patient records
* View all patient records
* Update existing patient records
* Delete patient records

### Data Validation

* Email format validation
* Numeric validation for blood test values
* Date of Birth validation

### AI-Based Health Prediction

The application predicts possible health conditions based on:

* Glucose Level
* Haemoglobin Level
* Cholesterol Level

Prediction categories:

* Healthy
* Diabetes Risk
* Heart Disease Risk

### Database Storage

* SQLite database for persistent storage
* Secure storage of patient information and prediction results

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Data Processing

* Pandas
* NumPy

### Model Persistence

* Joblib

---

## 📂 Project Structure

health-prediction-app-ai-ml/

├── app.py

├── database.py

├── ml_model.py

├── train_model.py

├── health_data.csv

├── requirements.txt

├── README.md

├── health_predictor.pkl

├── label_encoder.pkl

├── patients.db

├── screenshots/

│   ├── home.png

│   ├── add_patient.png

│   ├── view_patients.png

│   └── prediction_result.png

└── demo_video.mp4

---

## 📊 Dataset Information

The dataset contains the following attributes:

| Feature       | Description         |
| ------------- | ------------------- |
| Full Name     | Patient Name        |
| Date of Birth | Patient DOB         |
| Email Address | Contact Email       |
| Glucose       | Blood Glucose Level |
| Haemoglobin   | Haemoglobin Level   |
| Cholesterol   | Cholesterol Level   |
| Disease Label | Target Variable     |

---

## 🤖 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Input Features

* Glucose
* Haemoglobin
* Cholesterol

### Predicted Outputs

* Healthy
* Diabetes Risk
* Heart Disease Risk

### Why Random Forest?

* Good accuracy
* Handles small datasets effectively
* Resistant to overfitting
* Easy to implement and maintain

---

## 🚀 Installation and Setup

### Step 1: Clone Repository

git clone https://github.com/your-username/health-prediction-app-ai-ml.git

cd health-prediction-app-ai-ml

### Step 2: Create Virtual Environment

python -m venv venv

### Step 3: Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Step 4: Install Dependencies

pip install -r requirements.txt

### Step 5: Train Machine Learning Model

python train_model.py

### Step 6: Run Application

streamlit run app.py

### Step 7: Open Browser

http://localhost:8501/

---

## 🖥️ Application Workflow

1. User enters patient details.
2. System validates input data.
3. Machine learning model processes blood test values.
4. Predicted health condition is generated.
5. Prediction is stored in the database.
6. User can view, update, or delete records.



<img width="1920" height="1080" alt="home" src="https://github.com/user-attachments/assets/1033bbff-dbea-49ca-a5fa-c08913944b58" />



## 🔍 Challenges Faced

* Designing effective data validation mechanisms.
* Integrating machine learning predictions with CRUD operations.
* Managing SQLite database interactions efficiently.
* Creating a simple and user-friendly interface.


## 🔮 Future Enhancements

* Integration with real healthcare APIs.
* User authentication and authorization.
* Cloud deployment.
* Advanced disease prediction models.
* Data visualization dashboard.
* Email notification system.

---

## 👩‍💻 Author

**Shravani D G**

Bachelor of Engineering (Computer Science & Engineering)

AI/ML Enthusiast | Python Developer | Software Developer

GitHub: https://github.com/shra2115

LinkedIn: Add Your LinkedIn URL

---

