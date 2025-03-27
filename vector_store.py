import faiss
import numpy as np
import os

d = 512  # Embedding size

# Use IndexFlatIP for better similarity matching
base_index = faiss.IndexFlatIP(d)  # Inner Product similarity
index = faiss.IndexIDMap(base_index)

def add_embedding_to_faiss(embedding, child_id):
    """Add an embedding to FAISS with a unique ID."""
    embedding = np.array([embedding], dtype=np.float32)
    child_id = np.array([child_id], dtype=np.int64)
    index.add_with_ids(embedding, child_id)
    
    # Automatically save after each addition
    save_faiss_index()

def search_faiss(embedding, top_k=3, similarity_threshold=0.8):
    """Search for similar embeddings in FAISS with a similarity threshold."""
    embedding = np.array([embedding], dtype=np.float32)
    
    # Compute similarity instead of distance
    D, I = index.search(embedding, top_k)
    
    print(f"🔍 Similarity Scores: {D}")
    print(f"🆔 Matching IDs: {I}")
    
    # Filter matches based on similarity threshold
    valid_matches = [id for sim, id in zip(D[0], I[0]) if sim > similarity_threshold]
    
    return valid_matches if valid_matches else [-1]

def save_faiss_index(filename="data/embeddings/faiss_index.bin"):
    """Save FAISS index to a file, creating directory if needed."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    faiss.write_index(index, filename)
    print(f"✅ Index saved to {filename}")

def load_faiss_index(filename="data/embeddings/faiss_index.bin"):
    """Load FAISS index from a file."""
    global index
    if os.path.exists(filename):
        index = faiss.read_index(filename)
        print(f"✅ Index loaded from {filename}")
        return True
    print(f"❌ Index file {filename} not found")
    return False

# Ensure index is loaded on import
load_faiss_index()