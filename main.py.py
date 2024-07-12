import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model = YOLO(r'A:\yolov8\yolov8helmetdetection-main\best\best.pt')

def detect_helmets(frame):
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    class_file = open("coco1.txt", "r")
    class_list = class_file.read().split("\n")
    
    for index, row in px.iterrows():
        x1, y1, x2, y2, _, d = map(int, row)
        c = class_list[d]
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)

    return frame

if __name__ == "__main__":
    image_path = "A:\\yolov8\\yolov8helmetdetection-main\\helmet2.jpg"  # Replace with the path to your image
    image = cv2.imread(image_path)

    if image is not None:
        image = cv2.resize(image, (1020, 500))
        output_frame = detect_helmets(image)

        cv2.imshow("Detected Helmets", output_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image not found.")

