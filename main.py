import sys
from face_detection import detect_face
from embeddings import extract_embedding
from vector_store import add_embedding_to_faiss, search_faiss
from database import insert_child_metadata, create_metadata_table
from storage import store_encrypted_image
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def register_lost_child(image_url, name, age, gender, guardian_contact):
    face = detect_face(image_url)
    if face is None:
        print("No face detected.")
        return
    
    embedding = extract_embedding(face)
    child_id = hash(name + str(age)) % 1000000  # Generate unique ID
    add_embedding_to_faiss(embedding, child_id)
    
    encrypted_image_path = store_encrypted_image(image_url, child_id)
    insert_child_metadata(name, age, gender, guardian_contact, child_id, encrypted_image_path)
    
    print(f"Child registered successfully with ID: {child_id}")

def identify_found_child(image_url):
    face = detect_face(image_url)
    if face is None:
        print("No face detected.")
        return
    
    embedding = extract_embedding(face)
    matches = search_faiss(embedding, top_k=5, similarity_threshold=0.7)
    
    if matches[0] == -1:
        print("No match found.")
        return
    
    print(f"Match found! Possible Child IDs: {matches}")

if __name__ == "__main__":
    action = sys.argv[1]  # "register" or "identify"
    image_url = sys.argv[2]
    
    if action == "register":
        name, age, gender, guardian_contact = sys.argv[3:7]
        register_lost_child(image_url, name, int(age), gender, guardian_contact)
    elif action == "identify":
        identify_found_child(image_url)