import cv2 
from pprint import pprint
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

#read

cap=cv2.VideoCapture(0)
#print(cap)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model(frame)   
    annotated_frame = results[0].plot()
    cv2.imshow("LiveCamera",annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    #if cv2.waitKey(0):
    #    break
    #if cv2.waitKey(1) :
    #    break    
