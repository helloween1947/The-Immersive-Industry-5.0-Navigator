from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from twin import generate_twin_data
from voice import process_command
from ml_client import get_predictions

app = FastAPI()

# 🔥 CORS FIX (REQUIRED FOR REACT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🏠 Home Route
@app.get("/")
def home():
    return {"message": "Backend running successfully"}

# 🔹 Digital Twin API
@app.get("/twin/")
def twin():
    data = generate_twin_data()
    return data

# 🔹 Voice Command API
@app.post("/voice/")
def voice(input: dict):
    response = process_command(input["text"])
    return response

# 🔹 YOLO Detection API
@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    
    # Save uploaded image
    file_location = "temp.jpg"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get predictions from YOLO
    result = get_predictions(file_location)

    # OPTIONAL: Add severity logic
    for d in result["detections"]:
        if d["confidence"] > 0.8:
            d["severity"] = "HIGH"
        else:
            d["severity"] = "LOW"

    return {
        "status": "success",
        "detections": result["detections"]
    }