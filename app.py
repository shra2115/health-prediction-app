import streamlit as st
import pandas as pd
import re
from database import *
from ml_model import *

create_table()

st.title("Health Prediction Application")

menu = ["Add Patient","View Patients","Delete Patient"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Patient":
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    email = st.text_input("Email")
    glucose = st.number_input("Glucose")
    haemoglobin = st.number_input("Haemoglobin")
    cholesterol = st.number_input("Cholesterol")

    if st.button("Predict & Save"):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            st.error("Invalid Email")
        else:
            remarks = predict_disease(glucose, haemoglobin, cholesterol)
            add_patient(name, str(dob), email, glucose, haemoglobin, cholesterol, remarks)
            st.success(f"Prediction: {remarks}")

elif choice == "View Patients":
    data = view_all()
    df = pd.DataFrame(data, columns=["ID","Name","DOB","Email","Glucose","Haemoglobin","Cholesterol","Remarks"])
    st.dataframe(df)

elif choice == "Delete Patient":
    pid = st.number_input("Patient ID", step=1)
    if st.button("Delete"):
        delete_patient(pid)
        st.success("Deleted Successfully")
