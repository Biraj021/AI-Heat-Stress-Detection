"""
AI Heat Stress Detection
Backend Configuration
"""

from pathlib import Path


# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent


PROJECT_DIR = BASE_DIR.parent



# -----------------------------
# Flask Server Settings
# -----------------------------

HOST = "0.0.0.0"

PORT = 5000

DEBUG = True



# -----------------------------
# AI Model Path
# -----------------------------

MODEL_PATH = (
    PROJECT_DIR
    / "ai"
    / "heat_model.pkl"
)



# -----------------------------
# Sensor Data Storage
# -----------------------------

DATA_FOLDER = (
    BASE_DIR
    / "data"
)


DATA_FILE = (
    DATA_FOLDER
    / "sensor_data.csv"
)



# Create data folder automatically

DATA_FOLDER.mkdir(
    exist_ok=True
)