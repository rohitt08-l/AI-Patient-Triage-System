import joblib
import pandas as pd
from logger_config import setup_logger

logger = setup_logger("prediction")

model = joblib.load("models/triage_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")
feature_names = joblib.load("models/feature_names.pkl")


def predict_triage(patient_data_dict):
    logger.info(f"Received patient input: {patient_data_dict}")

    input_df = pd.DataFrame(
        [patient_data_dict],
        columns=feature_names
    )

    prediction = model.predict(input_df)
    label = encoder.inverse_transform(prediction)[0]

    logger.info(f"Predicted triage level: {label}")

    return label