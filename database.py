import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ypur-password",
        database="lost_child_db"
    )

def create_metadata_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Children_Metadata (
        child_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender VARCHAR(10),
        guardian_contact VARCHAR(20),
        embedding_id VARCHAR(255),
        image_url VARCHAR(255),
        case_status VARCHAR(10) DEFAULT 'Open'
    )''')
    
    conn.commit()
    conn.close()

def insert_child_metadata(name, age, gender, guardian_contact, embedding_id, image_url):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO Children_Metadata (name, age, gender, guardian_contact, embedding_id, image_url) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, age, gender, guardian_contact, embedding_id, image_url))
    
    conn.commit()
    conn.close()
