import torch
import cv2
import numpy as np
from facenet_pytorch import InceptionResnetV1

model = InceptionResnetV1(pretrained='vggface2').eval()

def extract_embedding(face):
    face_resized = cv2.resize(face, (160, 160)) / 255.0
    face_tensor = torch.tensor(face_resized).permute(2, 0, 1).unsqueeze(0).float()
    
    with torch.no_grad():
        embedding = model(face_tensor)
    
    return embedding.numpy().flatten()
