import os
import shutil
from encryption import encrypt_image, decrypt_image

IMAGE_STORAGE_PATH = "data/images/"

def store_encrypted_image(image_url, child_id):
    encrypted_path = os.path.join(IMAGE_STORAGE_PATH, f"{child_id}.enc")
    encrypt_image(image_url, encrypted_path)
    return encrypted_path

def retrieve_encrypted_image(encrypted_path, output_path):
    decrypt_image(encrypted_path, output_path)
