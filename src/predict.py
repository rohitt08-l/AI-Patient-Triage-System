# src/predict.py
import joblib


model = joblib.load("models/triage_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")


def predict_triage(patient_data):
    prediction = model.predict([patient_data])
    label = encoder.inverse_transform(prediction)
    return label[0]