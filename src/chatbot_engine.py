from symptom_extractor import extract_symptoms_from_text
from predict import predict_triage


def triage_chatbot_response(user_text):
    patient_data, symptoms = extract_symptoms_from_text(user_text)

    result = predict_triage(patient_data)

    recommendation = {
        "Critical": "Immediate emergency care required",
        "High": "Visit hospital within 1 hour",
        "Medium": "Doctor consultation recommended",
        "Low": "Home care is sufficient"
    }

    return {
        "symptoms": symptoms,
        "triage": result,
        "recommendation": recommendation[result]
    }