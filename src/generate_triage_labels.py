# src/generate_triage_labels.py
import pandas as pd

df = pd.read_csv("data/Final_Augmented_dataset_Diseases_and_Symptoms.csv")

critical_cols = [
    "shortness of breath",
    "sharp chest pain",
    "difficulty breathing",
    "seizures",
    "fainting",
    "apnea"
]

high_cols = [
    "fever",
    "fatigue",
    "vomiting",
    "chills",
    "wheezing",
    "sweating"
]

medium_cols = [
    "cough",
    "sore throat",
    "headache",
    "weakness"
]

def assign_triage(row):
    if any(row[col] == 1 for col in critical_cols if col in row.index):
        return "Critical"
    elif any(row[col] == 1 for col in high_cols if col in row.index):
        return "High"
    elif any(row[col] == 1 for col in medium_cols if col in row.index):
        return "Medium"
    return "Low"

df["triage_label"] = df.apply(assign_triage, axis=1)

df.to_csv("data/patient_triage.csv", index=False)

print("Triage dataset created successfully")
print(df["triage_label"].value_counts())