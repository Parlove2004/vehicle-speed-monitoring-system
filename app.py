import pandas as pd
import matplotlib.pyplot as plt
import random

# Generate sample data
data = {
    "vehicle_id": [f"V{i}" for i in range(1, 51)],
    "speed": [random.randint(30, 160) for _ in range(50)]
}

df = pd.DataFrame(data)

# Clean data
df = df[(df["speed"] > 0) & (df["speed"] < 200)]

# Speed classification
def classify_speed(speed):
    if speed <= 80:
        return "Within Limit (80)"
    elif speed <= 100:
        return "Within Limit (100)"
    else:
        return "Overspeeding"

df["status"] = df["speed"].apply(classify_speed)

# Visualization
df["status"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Vehicle Speed Analysis")
plt.ylabel("")
plt.show()
