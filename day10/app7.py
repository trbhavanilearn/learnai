import ultralytics
from ultralytics import YOLO
import cv2
from pprint import pprint

ultralytics.checks()

model = YOLO("yolov8n.pt")
print(f"Model Architecture Task: {model.task}")

results = model("roadtraffic.jpg")
pprint("Inference step complete.")