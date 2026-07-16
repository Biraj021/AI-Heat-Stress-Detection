import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==========================
# Load Dataset
# ==========================

DATASET = "dataset.csv"

df = pd.read_csv(DATASET)


print("\nDataset Loaded")
print(df.head())


# ==========================
# Features and Target
# ==========================

X = df[
    [
        "AmbientTemp",
        "Humidity"
    ]
]


y = df[
    "HeatStress"
]


# ==========================
# Split Data
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================
# Create Model
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train

model.fit(
    X_train,
    y_train
)


# ==========================
# Test Model
# ==========================

prediction = model.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    prediction
)


print("\nModel Accuracy:")
print(
    accuracy * 100,
    "%"
)


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        prediction
    )
)


# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    "heat_model.pkl"
)


print("\nModel saved successfully:")
print("heat_model.pkl")