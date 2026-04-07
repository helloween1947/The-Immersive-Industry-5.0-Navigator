import random

def generate_twin_data():
    temp = random.randint(30, 90)

    return {
        "temperature": temp,
        "pressure": random.randint(50, 120),
        "vibration": round(random.uniform(0.1, 1.0), 2),
        "status": "CRITICAL" if temp > 75 else "NORMAL",
        "alert": "⚠ Overheating detected" if temp > 75 else "All systems stable"
    }