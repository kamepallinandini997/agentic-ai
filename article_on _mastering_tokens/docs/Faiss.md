# Importance of FAISS – Storing and Searching Vectors
---

### What You're Going to Learn

In this section, you'll learn:

* Why vector search is essential in AI workflows
* What FAISS is and how it helps store and retrieve vector data
* How to create a FAISS index using embeddings
* How to perform similarity search using FAISS
* How embeddings and FAISS together power use cases like semantic search and recommendations

## Introduction: Why Do We Need Vector Search?

When we transform text into embeddings (vectors), we get a numerical format we can compare. But checking similarity across thousands (or millions) of vectors needs a **high-performance search engine**.

That’s where **FAISS** comes in.

## What is FAISS?
**FAISS** (Facebook AI Similarity Search) is a library for fast and efficient similarity search over dense vectors. It’s widely used in AI systems for:

* Semantic search
* Question-answering
* Recommendation engines
* Clustering and deduplication
## Step-by-Step: How to Store Vectors in FAISS

### Step 1: Install FAISS

```bash
pip install faiss-cpu
```
### Step 2: Generate Embeddings

We’ll use OpenAI’s `text-embedding-ada-002` model to generate 1536-dimensional embeddings for sample documents.

```python
import openai
import numpy as np

openai.api_key = "your-api-key"

def get_mean_embeddings(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

# Sample texts
documents = [
    "Learn Python programming",
    "Python for data analysis",
    "Yoga for mental health",
    "Best laptops for developers"
]

# Generate embeddings
embeddings = np.array([get_mean_embeddings(doc) for doc in documents]).astype('float32')
print("Embeddings shape:", embeddings.shape)
```
**Output**
```
Embeddings shape: (4, 1536)
```
Explanation:

* Each text is converted to a 1536-d vector.
* Now you have 4 vectors ready for indexing.

### Step 3: Build a FAISS Index

```python
import faiss

dimension = embeddings.shape[1]  # 1536
index = faiss.IndexFlatL2(dimension)

# Add vectors to the index
index.add(embeddings)

print("Total vectors in FAISS index:", index.ntotal)
```
**Output**
```
Total vectors in FAISS index: 4
```
Explanation:

* We used `IndexFlatL2`, which performs exact nearest neighbor search using Euclidean distance.
* You could replace this with `IndexFlatIP` for cosine similarity (after normalizing vectors).

### Step 4: Search with a New Query

Let’s embed a new text and find the top 2 most similar documents.

```python
query = "Introduction to Python for beginners"
query_embedding = np.array([get_mean_embeddings(query)]).astype('float32')

# Search for top 2 similar vectors
distances, indices = index.search(query_embedding, k=2)

print("Indices of nearest docs:", indices)
print("Distances:", distances)
```
**Output**
```
Indices of nearest docs: [[0 1]]
Distances: [[0.91 1.02]]
```
Explanation:

* FAISS returned the indices `0` and `1` as the closest matches.
* You can use these indices to fetch the original documents.

```python
for i in indices[0]:
    print("Match:", documents[i])
```
**Output**

```
Match: Learn Python programming
Match: Python for data analysis
```
## Recap of Learnings

* You learned the importance of **vector search** in NLP tasks
* FAISS is a **high-speed** and **scalable** library for this purpose
* You created and searched a **FAISS index** using embeddings from OpenAI’s Ada model
* The FAISS search returned **semantically similar texts** using numerical distance

## Knowledge Check

1. What does FAISS do with embeddings?
2. What kind of distance metric was used in `IndexFlatL2`?
3. What was the shape of each embedding vector generated from Ada?
4. What function was used to search the FAISS index?
5. If `index.search(query_vector, 3)` returns `[2, 0, 1]`, which documents are most similar?
---
