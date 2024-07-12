Helmet and Seatbelt Detection Project
This project is designed to detect helmets and seatbelts from a image input using YOLOv8 models.

Prerequisites
Before you begin, ensure you have met the following requirements:

You have Python 3.6 or later installed.
You have pip installed.
Installation

bash
Copy code
pip install opencv-python pandas ultralytics cvzone numpy
Usage
Place your trained model files (best.pt) in the project directory.

Update the paths to your  file and model files in main.py.

Run the project:



python main.py
main.py
Ensure main.py includes the following imports:

python
Copy code
import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
Project Structure
css
Copy code
helmet-seatbelt-detection/
├── helmet_best.pt
├── seatbelt_best.pt
├── main.py
├── README.md
Contributing
Contributions are always welcome! Please follow these steps:

License
This project is licensed under the MIT License. See the LICENSE file for more information.
