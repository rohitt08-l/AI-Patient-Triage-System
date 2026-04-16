import re
import joblib

feature_names = joblib.load("models/feature_names.pkl")


def extract_symptoms_from_text(user_text: str):
    user_text = user_text.lower()

    patient_data = {feature: 0 for feature in feature_names}

    keyword_mapping = {
        "fever": "fever",
        "cough": "cough",
        "chest pain": "chest pain",
        "breathing": "shortness of breath",
        "shortness of breath": "shortness of breath",
        "fatigue": "fatigue",
        "headache": "headache",
        "vomiting": "vomiting",
        "wheezing": "wheezing",
        "fainting": "fainting",
    }

    detected_symptoms = []

    for keyword, feature in keyword_mapping.items():
        if keyword in user_text and feature in patient_data:
            patient_data[feature] = 1
            detected_symptoms.append(feature)

    return patient_data, detected_symptoms