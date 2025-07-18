# Deep Dive into FAISS

## What we're Going to Learn

In this section, we'll go beyond the basics and:

- Understand the internal architecture of FAISS and how it indexes vectors
- Learn the different types of FAISS indexes (flat, quantized, inverted file, etc.)
- Explore advanced operations like filtering, updating, deleting, and saving indexes
- Learn what you can build using FAISS: semantic search engines, recommendation systems, similarity ranking, and more

---
## Why Go Deeper Into FAISS?

Basic indexing and searching is just the start. FAISS is powerful because it offers various indexing strategies and operations to make your search:

- **Faster** (with quantization and compression)
- **Scalable** (handle millions of vectors efficiently)
- **More intelligent** (filter, update, delete vectors dynamically)

By understanding FAISS in more depth, you can optimize your AI systems for real-world performance.

## What Can You Do With FAISS?

Here’s a list of common use cases where FAISS is applied:

| Use Case                         | Description |
|----------------------------------|-------------|
| Semantic Search                  | Retrieve documents based on meaning, not keywords |
| Duplicate Detection              | Find near-identical records in large datasets |
| Recommendation Systems           | Suggest similar products, movies, or users |
| Similarity Scoring               | Rank documents or texts by how close they are to a given input |
| Clustering or Grouping Vectors   | Perform grouping or topic detection by clustering embeddings |
| Chat Retrieval                   | Fetch relevant past chat history based on current query |
| Real-time Search Engines         | Fast retrieval even at scale using compressed indexes |

## Different Index Types in FAISS

FAISS offers several index types depending on your needs.

### 1. IndexFlatL2

- **Simple and accurate**
- Stores all vectors as-is
- Uses Euclidean distance

```python
index = faiss.IndexFlatL2(dimension)
```
###  2. IndexFlatIP

* Uses **inner product** (can be adapted to cosine similarity)
* Normalize vectors before adding

```python
def normalize(vectors):
    faiss.normalize_L2(vectors)
    return vectors

normalized_vectors = normalize(embeddings.copy())
index = faiss.IndexFlatIP(dimension)
index.add(normalized_vectors)
```

### 3. IndexIVFFlat

* **Inverted file index**
* Trains on a subset, then clusters vectors
* Faster for large datasets

```python
quantizer = faiss.IndexFlatL2(dimension)
index = faiss.IndexIVFFlat(quantizer, dimension, nlist=100)
index.train(embeddings)
index.add(embeddings)
```

### 4. IndexPQ (Product Quantization)

* Compresses vectors for memory efficiency
* Useful when storing millions of vectors

```python
index = faiss.IndexPQ(dimension, m=8, nbits=8)
index.train(embeddings)
index.add(embeddings)
```
## Advanced Operations in FAISS

### Saving and Loading an Index

```python
faiss.write_index(index, "index_file.faiss")
loaded_index = faiss.read_index("index_file.faiss")
```
### Removing Vectors by ID (with IDMap)

To support deletion, wrap index in an ID map.

```python
index = faiss.IndexIDMap(faiss.IndexFlatL2(dimension))
ids = np.array([101, 102, 103, 104])
index.add_with_ids(embeddings, ids)

# Remove a vector
index.remove_ids(np.array([102]))
```
### Updating Vectors (Re-adding with Same ID)

To update a vector, remove it and add the new version with the same ID.

```python
index.remove_ids(np.array([104]))
index.add_with_ids(new_embedding, np.array([104]))
```
## Recap of Learnings
* FAISS offers more than just `IndexFlatL2`; you have options like IVFFlat, FlatIP, PQ, and more
* You can normalize vectors for cosine similarity
* You can save, load, update, and delete vectors in a FAISS index
* FAISS can power real-world applications like semantic search, recommendations, and clustering

With these tools, FAISS becomes not just a library, but the **core engine behind many modern AI systems**.

## Knowledge Check

1. What’s the difference between `IndexFlatL2` and `IndexIVFFlat`?
2. How can you achieve cosine similarity using FAISS?
3. How do you delete a specific vector from a FAISS index?
4. When should you use `IndexPQ`?
5. What are some real-world use cases for FAISS?
