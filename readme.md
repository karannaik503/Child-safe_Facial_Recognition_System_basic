# **Child Safety Facial Recognition System**

This project is designed to help identify and reunite lost children using **facial recognition**. The system allows users to **register lost children** by storing their face embeddings and **identify found children** by matching their images against the database.

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Workflow](#workflow)
- [Installation & Setup](#installation--setup)
- [Prepare Directories](#prepare-directories)
- [Running the System](#running-the-system)
- [Automating Execution](#automating-execution)
- [Directory Structure](#directory-structure)

---

## **Project Overview**
The system consists of the following key functionalities:
1. **Register a Lost Child** - Stores the child's details, extracts facial embeddings, and saves encrypted images.
2. **Identify a Found Child** - Compares facial embeddings of a found child against the database.
3. **Secure Data Storage** - Uses FAISS for fast similarity search and AES encryption for image security.

---

## **Workflow**
### **1. Registering a Lost Child**
1. Detects a face from the provided image.
2. Extracts a **512-dimensional embedding** from the face.
3. Stores the embedding in the **FAISS index**.
4. Encrypts and stores the image securely.
5. Saves child metadata (name, age, guardian contact, image path) in **MySQL database**.

### **2. Identifying a Found Child**
1. Detects a face from the provided image.
2. Extracts the facial embedding.
3. Searches the **FAISS index** for the most similar embeddings.
4. If a match is found, retrieves child details from the **MySQL database**.
5. Displays the matching child ID(s) and associated details.

---

## **Installation & Setup**

### **1. Install Dependencies**
Ensure Python 3.8+ is installed. Install required libraries:
```bash
pip install mysql-connector-python opencv-python numpy torch torchvision torchaudio facenet-pytorch mtcnn faiss-cpu pycryptodome
```
> **For GPU acceleration**, install `faiss-gpu` instead of `faiss-cpu`:
```bash
pip install faiss-gpu
```

or simply install the dependencies from the requirements.txt
```bash
pip install -r requirements.txt
```
### **2. Setup MySQL Database**
Start MySQL and create the required database:
```bash
mysql -u root -p
```
Run these SQL commands:
```sql
CREATE DATABASE child_safety;
USE child_safety;

CREATE TABLE IF NOT EXISTS Children_Metadata (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    guardian_contact VARCHAR(20),
    embedding_id VARCHAR(255),
    image_url VARCHAR(255),
    case_status VARCHAR(10) DEFAULT 'Open'
);
```

Alternatively, run the Python script to create the table:
```bash
python -c "from database import create_metadata_table; create_metadata_table()"
```

### **3. Configure MySQL Credentials**
Update the **`config.py`** and **`database.py`** files with your MySQL username and password:

#### **config.py**
```python
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",  # Change this to your MySQL username
    "password": "your-password",  # Change this to your MySQL password
    "database": "child_safety"
}
```

#### **database.py**
```python
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change this to your MySQL username
        password="your-password",  # Change this to your MySQL password
        database="child_safety"
    )
```

---

## **Prepare Directories**
Create necessary directories for image storage and embeddings:
```bash
mkdir -p data/embeddings data/images data/test_images
```
Ensure the following project directory structure:
```bash
CHILD_SAFE_RECOGNITION_BASIC/
│-- data/
│   │-- embeddings/
│   │-- images/
│   │-- test_images/
│   └-- faceenv/
│-- config.py
│-- database.py
│-- embeddings.py
│-- encryption.py
│-- face_detection.py
│-- main.py
│-- run.sh
│-- storage.py
│-- utils.py
│-- vector_store.py
```

---

## **Running the System**
### **1. Register a Lost Child**
Run the following command:
```bash
python main.py register lost_abhi.jpg "Abhishikt" 9 "M" "+917899999884"
```
**Process:**
1. Extracts facial features from `lost_abhi.jpg`.
2. Stores embeddings in FAISS.
3. Encrypts and saves the image.
4. Saves metadata in MySQL.

### **2. Identify a Found Child**
Run the following command:
```bash
python main.py identify abhi.jpg
```
**Process:**
1. Extracts facial features from `abhi.jpg`.
2. Searches the FAISS database.
3. Displays matching child ID(s) if found.

---

## **Automating Execution**
To automate both registration and identification, create a `run.sh` script:
```bash
#!/bin/bash
python main.py register lost_abhi.jpg "Abhishikt" 9 "M" "+917899999884"
python main.py identify abhi.jpg
```
Make it executable:
```bash
chmod +x run.sh
```
Run:
```bash
./run.sh
```

---

## **Directory Structure**
```bash
CHILD_SAFE_RECOGNITION_BASIC/
│-- data/
│   │-- embeddings/
│   │-- images/
│   │-- test_images/
│-- config.py
│-- database.py
│-- embeddings.py
│-- encryption.py
│-- face_detection.py
│-- main.py
│-- run.sh
│-- storage.py
│-- utils.py
│-- vector_store.py
```

---

## **Conclusion**
This project provides an **efficient lost-and-found system** for children using **facial recognition** and **secure image storage**. 

**Future Improvements:**
- Implement a web-based UI for easy access.
- Improve search algorithms for better accuracy.
- Add real-time video processing for live identification.
- real-time notification feature through whatsapp or SMS
