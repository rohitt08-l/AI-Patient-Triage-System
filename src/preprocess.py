# src/preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess():
    df = pd.read_csv("data/patient_triage.csv")

    X = df.drop(columns=["diseases", "triage_label"], errors="ignore")
    y = df["triage_label"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, encoder