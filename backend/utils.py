"""
AI Heat Stress Detection
Backend Utility Functions
"""

from pathlib import Path
from datetime import datetime

import joblib
import pandas as pd

from config import MODEL_PATH, DATA_FILE



# -----------------------------
# Load AI Model
# -----------------------------

def load_model():

    """
    Load trained AI model
    """

    if not Path(MODEL_PATH).exists():

        raise FileNotFoundError(
            "AI model not found. Train the model first."
        )


    return joblib.load(MODEL_PATH)



# Load model once

model = load_model()



# -----------------------------
# Predict Heat Stress
# -----------------------------

def predict_heat_stress(
        ambient_temp,
        humidity
):

    """
    Predict Low / Medium / High heat stress
    """


    input_data = pd.DataFrame(
        [
            {
                "AmbientTemp": ambient_temp,
                "Humidity": humidity
            }
        ]
    )


    prediction = model.predict(
        input_data
    )


    return prediction[0]



# -----------------------------
# Save Sensor Data
# -----------------------------

def save_sensor_data(
        ambient_temp,
        humidity,
        heat_stress
):

    """
    Store sensor readings in CSV
    """


    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    new_record = pd.DataFrame(
        [
            {
                "Timestamp": timestamp,
                "AmbientTemp": ambient_temp,
                "Humidity": humidity,
                "HeatStress": heat_stress
            }
        ]
    )


    # Create CSV if missing

    if not Path(DATA_FILE).exists():

        new_record.to_csv(
            DATA_FILE,
            index=False
        )


    else:

        old_data = pd.read_csv(
            DATA_FILE
        )


        updated_data = pd.concat(
            [
                old_data,
                new_record
            ],
            ignore_index=True
        )


        updated_data.to_csv(
            DATA_FILE,
            index=False
        )


    return True