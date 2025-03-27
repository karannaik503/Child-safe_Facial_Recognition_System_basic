from Crypto.Cipher import AES
import os

KEY = os.urandom(32)  # Store securely

def encrypt_image(input_path, output_path):
    cipher = AES.new(KEY, AES.MODE_GCM)
    
    with open(input_path, 'rb') as f:
        data = f.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    with open(output_path, 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)

def decrypt_image(input_path, output_path):
    with open(input_path, 'rb') as f:
        nonce, tag, ciphertext = f.read(16), f.read(16), f.read()[32:]
    
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(output_path, 'wb') as f:
        f.write(data)
