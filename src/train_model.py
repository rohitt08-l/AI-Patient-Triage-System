from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

from preprocess import load_and_preprocess
from logger_config import setup_logger

logger = setup_logger("training")


def train():
    try:
        logger.info("Started model training pipeline")

        X_train, X_test, y_train, y_test, encoder = load_and_preprocess()
        logger.info("Dataset loaded successfully")
        logger.info(f"Train shape: {X_train.shape}")
        logger.info(f"Test shape: {X_test.shape}")

        model = RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        )

        logger.info("Training Random Forest model...")
        model.fit(X_train, y_train)

        logger.info("Model training completed")

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        logger.info(f"Model accuracy: {accuracy * 100:.2f}%")

        print(f"\nAccuracy: {accuracy * 100:.2f}%")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        os.makedirs("models", exist_ok=True)

        logger.info("Saving model artifacts...")

        joblib.dump(model, "models/triage_model.pkl")
        joblib.dump(encoder, "models/label_encoder.pkl")
        joblib.dump(
            X_train.columns.tolist(),
            "models/feature_names.pkl"
        )

        logger.info("All model artifacts saved successfully")
        print("\nModel artifacts saved successfully")

    except Exception as e:
        logger.error(f"Training failed: {str(e)}")
        raise


if __name__ == "__main__":
    train()