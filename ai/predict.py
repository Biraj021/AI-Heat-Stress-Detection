import joblib
import pandas as pd


# ==========================
# Load AI Model
# ==========================

model = joblib.load(
    "heat_model.pkl"
)


# ==========================
# Test Sensor Input
# ==========================

sensor_data = pd.DataFrame(
    [
        {
            "AmbientTemp": 38.0,
            "Humidity": 90
        }
    ]
)


# ==========================
# Prediction
# ==========================

prediction = model.predict(
    sensor_data
)[0]


# ==========================
# Confidence
# ==========================

probability = model.predict_proba(
    sensor_data
)


confidence = max(probability[0]) * 100



print("==============================")
print("AI Heat Stress Prediction")
print("==============================")


print(
    "Ambient Temperature:",
    sensor_data["AmbientTemp"][0],
    "°C"
)


print(
    "Humidity:",
    sensor_data["Humidity"][0],
    "%"
)


print(
    "Prediction:",
    prediction
)


print(
    "Confidence:",
    round(confidence,2),
    "%"
)