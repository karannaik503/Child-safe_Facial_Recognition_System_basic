import cv2
import numpy as np
from mtcnn import MTCNN

detector = MTCNN()

def detect_face(image_url):
    image = cv2.imread(image_url)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    detections = detector.detect_faces(image_rgb)

    if not detections:
        return None

    x, y, width, height = detections[0]['box']
    face = image_rgb[y:y+height, x:x+width]
    
    return face
