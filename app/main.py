import streamlit as st
import os
import sys
import joblib

# Add src folder to path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from predict import predict_triage
from logger_config import setup_logger

logger = setup_logger("streamlit")

feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(page_title="AI Patient Triage System", layout="wide")

st.title("AI-Based Patient Triage System")
st.markdown("Enter patient symptoms to predict urgency level.")

st.subheader("Patient Symptom Input")

fever = st.selectbox("Fever", [0, 1], key="fever")
cough = st.selectbox("Cough", [0, 1], key="cough")
chest_pain = st.selectbox("Chest Pain", [0, 1], key="chest_pain")
shortness_of_breath = st.selectbox(
    "Shortness of Breath",
    [0, 1],
    key="sob"
)
fatigue = st.selectbox("Fatigue", [0, 1], key="fatigue")
headache = st.selectbox("Headache", [0, 1], key="headache")

if st.button("Predict Triage", key="predict_btn"):
    logger.info("Predict button clicked")

    patient_data = {feature: 0 for feature in feature_names}

    # Safe feature mapping
    if "fever" in patient_data:
        patient_data["fever"] = fever
    if "cough" in patient_data:
        patient_data["cough"] = cough
    if "chest pain" in patient_data:
        patient_data["chest pain"] = chest_pain
    if "shortness of breath" in patient_data:
        patient_data["shortness of breath"] = shortness_of_breath
    if "fatigue" in patient_data:
        patient_data["fatigue"] = fatigue
    if "headache" in patient_data:
        patient_data["headache"] = headache

    result = predict_triage(patient_data)

    # Emergency override
    if chest_pain == 1 and shortness_of_breath == 1:
        logger.warning("Emergency override triggered")
        result = "Critical"

    logger.info(f"Prediction displayed in UI: {result}")

    st.success(f"Predicted Triage Level: {result}")

    if result == "Critical":
        st.error("Immediate emergency care required")
    elif result == "High":
        st.warning("Visit hospital within 1 hour")
    elif result == "Medium":
        st.info("Doctor consultation recommended")
    else:
        st.success("Home care is sufficient")