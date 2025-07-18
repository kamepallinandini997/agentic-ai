# Understanding and Integrating FAISS and MongoDB
### What You’re Going to Learn

* Why MongoDB is needed alongside FAISS
* How to set up a **free MongoDB Atlas cluster** online
* How to allow your **local Python/Faiss code** to access this remote database
* How to **store metadata** in MongoDB and **vector embeddings** in FAISS
* How to link them together using unique IDs

## Why Use MongoDB with FAISS?

FAISS is excellent at storing **vectors** and searching through them quickly.  
But it **doesn’t store metadata** like:

- Document titles
- File names or tags
- Chunked text or descriptions
- Created date or author

MongoDB, being a NoSQL document store, is perfect for keeping all this structured metadata.

We use MongoDB for:  
- Fast filtering and searching based on fields (like tags, sources, or user)  
- Linking vector data to real-world meaning  
- Keeping our app’s data organized and queryable

---

## Set Up a Free MongoDB Atlas Cluster (Cloud)

1. Go to [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)  
2. Click **Start Free**, sign in using Google or email  
3. Select **Shared Cluster (Free Tier)** → Choose AWS/Google Cloud/Azure + region  
4. Cluster name: e.g. `resume-cluster`  
5. **Create Database User**  
   - Username: `myuser`  
   - Password: `mypassword123`  
6. Under **Network Access**  
   - Click “Add IP Address”  
   - Choose **“My Current IP”** or allow all using `0.0.0.0/0` (for learning/demo use only)

## Step 3: Get the MongoDB URI

1. After cluster is ready → Click **Connect**  
2. Choose **Connect Your Application**  
3. Copy the URI — it will look like this:

```
mongodb+srv://myuser\:mypassword123\@resume-cluster.mongodb.net/?retryWrites=true\&w=majority

```

Modify the URI in your Python code as needed.

## Step 4: Code to Store in MongoDB and FAISS

``` python
import numpy as np
import faiss
from pymongo import MongoClient

# ---- MongoDB Setup ----
MONGO_URI = "your_mongo_uri_here"
client = MongoClient(MONGO_URI)
db = client["resume_db"]
collection = db["resume_chunks"]

# ---- FAISS Setup ----
dimension = 384
index = faiss.IndexFlatL2(dimension)

# ---- Sample Data ----
chunk_text = "Skilled in Python, Pandas, and REST APIs"
vector = np.random.rand(dimension).astype("float32")

# ---- Step 1: Save to FAISS ----
index.add(np.array([vector]))

# ---- Step 2: Save to MongoDB ----
metadata = {
    "_id": "chunk_001",     # Use your own ID logic
    "text": chunk_text,
    "skills": ["Python", "Pandas", "REST"],
    "source": "resume.pdf"
}
collection.insert_one(metadata)
```
###  Output 

```bash
FAISS index total vectors: 1
MongoDB document inserted: chunk_001
```
## Recap

* **FAISS** handles raw vector data and nearest-neighbor search
* **MongoDB** stores meaningful metadata like text, file names, and tags
* We linked both systems using a unique `_id` or custom string like `"chunk_001"`
* The two systems **work in parallel**, one for search (FAISS), the other for structured queries (MongoDB)

## Knowledge Check
1. What kind of data is stored in FAISS vs MongoDB?
2. Why is it important to store both vector and metadata separately?
3. What does `IndexFlatL2` in FAISS do?
4. Why is it recommended to whitelist your IP in MongoDB Atlas?
5. What would happen if you stored metadata in FAISS directly?
6. How can you retrieve a document’s metadata using only a vector search result?
7. What MongoDB collection and field names did we use in the code?
8. What is the purpose of using `_id` while storing metadata in MongoDB?
9. How can you update a chunk’s metadata if its vector stays the same?
10. What would break if your `_id` in MongoDB doesn’t match the vector index?
