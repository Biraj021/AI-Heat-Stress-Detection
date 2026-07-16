from flask import Flask, request, jsonify
import pandas as pd
import joblib
from datetime import datetime
import os


# =====================================
# Flask Application
# =====================================

app = Flask(__name__)


# =====================================
# Load AI Model
# =====================================

MODEL_PATH = "../ai/heat_model.pkl"


try:
    model = joblib.load(MODEL_PATH)

    print("AI Model Loaded Successfully")

except Exception as e:

    print("Model Loading Failed:")
    print(e)

    model = None



# =====================================
# Sensor Data Storage
# =====================================

DATA_FOLDER = "data"

CSV_FILE = os.path.join(
    DATA_FOLDER,
    "sensor_data.csv"
)


os.makedirs(
    DATA_FOLDER,
    exist_ok=True
)



# Create CSV if not exists

if not os.path.exists(CSV_FILE):

    dataframe = pd.DataFrame(
        columns=[
            "Timestamp",
            "AmbientTemp",
            "Humidity",
            "HeatStress",
            "Confidence"
        ]
    )

    dataframe.to_csv(
        CSV_FILE,
        index=False
    )



# =====================================
# Home API
# =====================================

@app.route("/")
def home():

    return jsonify(
        {
            "Project":
            "AI Heat Stress Detection",

            "Status":
            "Running",

            "Model":
            "Random Forest AI"
        }
    )



# =====================================
# Prediction API
# =====================================

@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    try:

        # Receive ESP32 JSON

        data = request.get_json()


        temperature = float(
            data["AmbientTemp"]
        )


        humidity = float(
            data["Humidity"]
        )


        # Prepare AI input

        sensor_input = pd.DataFrame(
            [
                {
                    "AmbientTemp":
                    temperature,

                    "Humidity":
                    humidity
                }
            ]
        )



        # AI Prediction

        prediction = model.predict(
            sensor_input
        )[0]



        # Prediction Confidence

        probabilities = model.predict_proba(
            sensor_input
        )


        confidence = round(
            max(probabilities[0]) * 100,
            2
        )



        # Save sensor data

        new_data = pd.DataFrame(
            [
                {
                    "Timestamp":
                    datetime.now(),

                    "AmbientTemp":
                    temperature,

                    "Humidity":
                    humidity,

                    "HeatStress":
                    prediction,

                    "Confidence":
                    confidence
                }
            ]
        )


        new_data.to_csv(
            CSV_FILE,
            mode="a",
            header=False,
            index=False
        )



        # Response

        return jsonify(
            {
                "AmbientTemp":
                temperature,


                "Humidity":
                humidity,


                "HeatStress":
                prediction,


                "Confidence":
                str(confidence) + "%"

            }
        )



    except Exception as e:


        return jsonify(
            {
                "Error":
                str(e)
            }
        ), 400




# =====================================
# Start Server
# =====================================

if __name__ == "__main__":

    print("==============================")
    print("AI Heat Stress Backend")
    print("Server Starting...")
    print("==============================")


    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )