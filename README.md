# 🔥 AI Heat Stress Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![ESP32](https://img.shields.io/badge/ESP32-IoT-green?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)

</p>

---

# 📖 Overview

AI Heat Stress Detection System is an IoT + AI based smart monitoring system that continuously measures environmental conditions using an **ESP32** and **DHT22 Sensor**.

The sensor data is sent to a **Flask Backend**, where the **Heat Index** is calculated and an **AI Machine Learning model** predicts the Heat Stress Risk.

The prediction is displayed on a **real-time Streamlit Dashboard**, allowing users to monitor live conditions and receive instant alerts.

---

# 🚀 Project Features

✅ Real-time Temperature Monitoring

✅ Real-time Humidity Monitoring

✅ Automatic Heat Index Calculation

✅ AI-based Heat Stress Prediction

✅ Flask REST API

✅ ESP32 WiFi Communication

✅ CSV Data Storage

✅ Live Streamlit Dashboard

✅ Historical Charts

✅ Color-coded Risk Status

✅ Automatic Data Refresh

---

# 🏗 System Architecture

<p align="center">

<img src="docs/architecture.png" width="900">

</p>

---

# 🔄 Working Flow

```text
             DHT22 Sensor
                  │
                  ▼
          ESP32 Microcontroller
                  │
      Read Temperature & Humidity
                  │
                  ▼
        Connect using WiFi
                  │
                  ▼
     Send JSON to Flask Backend
                  │
                  ▼
     Calculate Heat Index
                  │
                  ▼
      AI Prediction Model
                  │
                  ▼
      Predict Risk Level
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
 Save Sensor Data        Streamlit Dashboard
   sensor_data.csv        Live Visualization
```

---

# 📂 Folder Structure

```text
AI-Heat-Stress-Detection
│
├── ai/
│   ├── dataset.csv
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── predict.py
│   └── heat_model.pkl
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── utils.py
│   └── data/
│       └── sensor_data.csv
│
├── dashboard/
│   └── dashboard.py
│
├── esp32/
│   └── heat_stress/
│       └── heat_stress.ino
│
├── docs/
│   └── architecture.png
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# ⚙ Technologies Used

| Technology | Purpose |
|------------|----------|
| ESP32 | IoT Controller |
| DHT22 | Temperature & Humidity Sensor |
| Python | Backend + AI |
| Flask | REST API |
| Streamlit | Dashboard |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| Joblib | Model Saving |
| Plotly | Interactive Charts |
| Requests | API Communication |

---

# 🤖 AI Prediction

The AI model predicts one of the following Heat Stress Levels.

| Heat Stress | Status |
|-------------|---------|
| 🟢 Low | Safe Environment |
| 🟡 Medium | Moderate Heat Stress |
| 🔴 High | Dangerous |
| 🚨 Critical | Immediate Action Required |

The prediction uses:

- Temperature
- Humidity
- Heat Index

---

# 📊 Dashboard

The Streamlit dashboard displays

- 🌡 Temperature
- 💧 Humidity
- 🔥 Heat Index
- 🤖 AI Prediction
- 📈 Historical Graph
- 📋 Recent Sensor Records
- 🚨 Critical Alert Messages

---

# 📡 API Endpoints

## POST

```
/predict
```

Receives

```json
{
    "AmbientTemp":35.2,
    "Humidity":65
}
```

Returns

```json
{
    "temperature":35.2,
    "humidity":65,
    "heat_index":42.7,
    "prediction":"High"
}
```

---

## GET

```
/health
```

Returns

```json
{
  "status":"Running"
}
```

---

# 💻 Installation

Clone Repository

```bash
git clone https://github.com/IndrajitDutta420/AI-Heat-Stress-Detection.git
```

Go to project

```bash
cd AI-Heat-Stress-Detection
```

Install requirements

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
cd backend

python app.py
```

---

# ▶ Train AI Model

```bash
cd ai

python train_model.py
```

---

# ▶ Run Dashboard

```bash
cd dashboard

streamlit run dashboard.py
```

---

# ▶ Upload ESP32 Code

Open

```
esp32/heat_stress/heat_stress.ino
```

Update

```
WiFi Name

WiFi Password

Server IP Address
```

Upload to ESP32.

---

# 📈 Heat Stress Levels

| Heat Index | Risk |
|------------|------|
| Below 27°C | Low |
| 27–32°C | Medium |
| 32–41°C | High |
| Above 41°C | Critical |

---

# 🚨 Critical Alert

When the AI predicts **Critical** the dashboard displays

```
🚨 CRITICAL HEAT STRESS

Move to a cool place immediately.

Drink water.

Avoid direct sunlight.

Seek medical assistance if symptoms continue.
```

---

# 📸 Project Demo

Add screenshots here.

```
docs/dashboard.png

docs/backend.png

docs/esp32.png
```

---

# 👨‍💻 Team

**Biraj Acherjee**

GitHub

https://github.com/Biraj021

---

**Indrajit Dutta**

GitHub

https://github.com/IndrajitDutta420

---

# ⭐ Future Improvements

- SMS Alert
- Email Notification
- Telegram Bot
- Buzzer Alarm
- GPS Location
- Cloud Database
- Firebase Integration
- Mobile Application
- Doctor Notification
- Weather API Integration

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you like this project, don't forget to Star the Repository.