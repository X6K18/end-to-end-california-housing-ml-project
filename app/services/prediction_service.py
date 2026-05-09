import os
import joblib
import numpy as np

# ====================================
# Base Directory
# ====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

# ====================================
# Model Paths
# ====================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "linear_regression_model",
    "linear_regression.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "linear_regression_model",
    "scaler.pkl"
)

# ====================================
# Load Model
# ====================================

regmodel = joblib.load(MODEL_PATH)

# ====================================
# Load Scaler
# ====================================

scaler = joblib.load(SCALER_PATH)

# ====================================
# Prediction Function
# ====================================

def predict_house_price(data: dict) -> float:

    features = np.array([
        data["MedInc"],
        data["HouseAge"],
        data["AveRooms"],
        data["AveBedrms"],
        data["Population"],
        data["AveOccup"],
        data["Latitude"],
        data["Longitude"]
    ]).reshape(1, -1)

    scaled_features = scaler.transform(features)

    prediction = regmodel.predict(scaled_features)[0]

    return round(float(prediction), 4)
