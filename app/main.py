import streamlit as st
import pandas as pd
import joblib
import os
import sys

# Add src path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from predict import predict_triage

st.set_page_config(page_title="AI Patient Triage System", layout="wide")

st.title("🏥 AI-Based Patient Triage System")
st.markdown("Enter patient symptoms to predict urgency level.")

st.subheader("🩺 Patient Symptom Input")

# Sample important symptoms for MVP
fever = st.selectbox("Fever", [0, 1])
cough = st.selectbox("Cough", [0, 1])
chest_pain = st.selectbox("Chest Pain", [0, 1])
shortness_of_breath = st.selectbox("Shortness of Breath", [0, 1])
fatigue = st.selectbox("Fatigue", [0, 1])
headache = st.selectbox("Headache", [0, 1])

if st.button("🔍 Predict Triage"):
    patient_data = [0] * 377  # total feature count in dataset

    # IMPORTANT: map selected important symptoms to correct indexes later
    # temporary MVP mapping
    patient_data[0] = fever
    patient_data[1] = cough
    patient_data[2] = chest_pain
    patient_data[3] = shortness_of_breath
    patient_data[4] = fatigue
    patient_data[5] = headache

    result = predict_triage(patient_data)

    # Emergency override
    if chest_pain == 1 and shortness_of_breath == 1:
        result = "Critical"

    st.success(f"🚨 Predicted Triage Level: {result}")

    if result == "Critical":
        st.error("⚠ Immediate emergency care required")
    elif result == "High":
        st.warning("🟠 Visit hospital within 1 hour")
    elif result == "Medium":
        st.info("🟡 Doctor consultation recommended")
    else:
        st.success("🟢 Home care is sufficient")