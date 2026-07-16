import random
import pandas as pd

random.seed(42)

data = []

for _ in range(1000):

    ambient_temp = round(random.uniform(24, 42), 1)
    humidity = random.randint(30, 100)

    # Heat Stress Rules
    if ambient_temp >= 38 or (ambient_temp >= 35 and humidity >= 80):
        heat_stress = "High"

    elif ambient_temp >= 32 or humidity >= 65:
        heat_stress = "Medium"

    else:
        heat_stress = "Low"

    data.append([
        ambient_temp,
        humidity,
        heat_stress
    ])

df = pd.DataFrame(
    data,
    columns=[
        "AmbientTemp",
        "Humidity",
        "HeatStress"
    ]
)

df.to_csv("dataset.csv", index=False)

print("\nDataset Created Successfully!\n")

print(df.head())

print("\nClass Distribution\n")
print(df["HeatStress"].value_counts())

print("\nDataset Information\n")
print(df.info())