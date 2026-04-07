from ultralytics import YOLO

# ✅ Load YOLO model (IMPORTANT: file must be in backend folder)
model = YOLO("yolov8n.pt")

def get_predictions(image_path):
    results = model(image_path)

    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            label = model.names[cls]

            detections.append({
                "label": label,
                "confidence": round(conf, 2),
                "bbox": [
                    int(x1),
                    int(y1),
                    int(x2 - x1),
                    int(y2 - y1)
                ]
            })

    return {"detections": detections}