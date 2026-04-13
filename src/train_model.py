# src/train_model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess import load_and_preprocess


def train():
    X_train, X_test, y_train, y_test, encoder = load_and_preprocess()

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"✅ Accuracy: {accuracy * 100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    # save model
    joblib.dump(model, "models/triage_model.pkl")
    joblib.dump(encoder, "models/label_encoder.pkl")

    print("✅ Model saved successfully")


if __name__ == "__main__":
    train()