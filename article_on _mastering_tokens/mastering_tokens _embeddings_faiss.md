# Article on Mastering Tokens, Embeddings,Vectors  Faiss and Mongo DB.

In this article, we are  going to learn how robots actually understand and respond  what you're saying.

- We’ll cover:
  - What are tokens and why they're important
  - What are embeddings and how they give meaning to text
  - What are vectors, and why we need vector search
  - Tools like FAISS and MongoDB

- ## Table of Contents:
	- Introduction 
	- Pre-requisites 
	- What are Tokens and Tokenization
	- Understanding importance of Embeddings and vectors
	- Practice on Embeddings and vectors
	- Importance of Faiss, storing and searching vectors  in Faiss
	- Deep Dive into FAISS
	- Understanding and Integrating FAISS and MongoDB
	- Practical Example: News Api
	- Conclusion

---
# Section 1: Introduction
This article will cover basic terminology. Understanding these terms will be crucial for grasping the concepts discussed in the article.

Let us take an example when you are trying to communicate with a machine and let's say you are asking it "Tell me how to bake a cake". 
But the machine not able to understand human language like we do. So here is the case where tokens,embeddings , vectors and rest everything comes into scenario. Let's breakdown it step by step:

### Tokens:
Lets take previous example : "Tell me how to bake a cake "

From above example each word is a token.

- words : ["Tell","me","how","to","bake","a","Cake"]
- sub words : ["Te","ll"]
- characters : ['T','e','l'.'l']
```
"Tell me how to bake a cake " is similar to "Tell how bake a cake to me"
 ```
So the machine will understand like this:
```
Sentence --> Words --> Sub-Words --> Characters
```
### Embeddings:
As we have discussed earlier - now the robot has tokens.But how will it understand what “bake” or “fun” means?.You can’t just tell a robot “bake means to cook” — it won’t understand that easily.So instead, we give the robot something called an embedding.

An embedding is like a magic number list that shows the meaning of a word.
For example:
| Word   |   Embedding (example)            |
|--------|----------------------------------|
| bake   |   [0.23, 0.98, 0.55, ...]        |
| cake   |   [0.72, 0.10, 0.88, ...]        |
| fun    |   [0.11, 0.99, 0.31, ...]        |

Each word is turned into a vector (a list of numbers), and similar words have similar number patterns.

So “bake” and “cook” will be close together in vector space.

### Vector Search:
Now imagine the robot has thousands of answers stored as vectors.When you ask a question like “how to bake a cake”, the robot:
- Converts your question into a vector using embeddings.
- Searches all its vectors to find the most similar ones.
- Gives you the best matching answer.

This kind of search is called vector search.
But there’s a small problem: Searching through thousands (or millions!) of vectors takes time.So we need a fast tool to help — and that’s where FAISS comes in.

### FAISS:
FAISS (Facebook AI Similarity Search) is like a best and fast search engine for vectors.

Imagine you have a library filled with books, and you want to find the one that’s most similar to your question.
- FAISS stores all the vectors.
- FAISS searches them really fast.
- FAISS returns the closest match.

This will save time and makes the  robot work effieciently.

### Mongo DB(No SQL):
Okay, so the robot found the matching answer using FAISS.But what about details like:

- Where did the answer come from?
- Who wrote it?
- What date was it published?

All that extra information (called metadata) is stored in MongoDB.

MongoDB is a database— it stores all the information related to each answer so we can show it to the user later and most commonly useful for semi-structured and unstructured data.
### Model:
A model is a mathematical function trained on data to understand and generate language. Think of it like a brain that has read lots of books and now predicts what comes next in a sentence.

**Common Use Cases & Applications:**
1. Text Generation
2. Chatbots & Virtual Assistants
3. Text Summarization
4. Education & Tutoring
### Language Model(LM):
Language Model (LM) is a computer program trained to understand by pattern of language and generate human understandable language.More over it is a program that  learns the patterns from reading thousands of books, websites, news articles.
LM's were built on Neural networks where models are inspired by the structure of humen brain.

- Common usecases:
    - Machine Translation
    - Speech Recognition
    - Natural Language Processing(NLP) and so on

And that program is a Language Model.

### Large LAnguage Model(LLM):
When an LM is trained on a huge data(eg : whole internet) we call it a Large Language Model or LLM.LLMs are very smart. They can write poems, answer questions, summarize books, Translate languages and much more!

* Example of LLM's:
    - GPT (like ChatGPT)
    - BERT (by Google)
    - LLaMA (by Meta)
    - Gemini (by Google)
    - Claude (by Anthropic)

### GPT:
GPT refers to Generative Pretrained Transformer.
* Generative - It can create new text like a story or answer
* Pretrainerd - It was already trained on tons of text before you used it
* Transformer - It helps to understand context and respond like a human

In other words GPT is used for NLP(Natural language processing) related tasks.
* common Use Cases:
    * Chatbots and voice assistants
    * Language translation
    * Data analysis
    * Coding
## Recap of What you've learnt

In this section, you’ve learned the core terminology and concepts required to understand how language models process and represent text:

* A **language model** is a trained system that generates human-like responses.
* A **tokenizer** breaks input text into smaller units called **tokens**.
* A **token** can be a word, sub-word, or symbol — it's the model’s basic unit of input.
* An **embedding** is a numerical vector that captures the meaning of a token.
* A **vector** is a list of numbers used to represent text in mathematical space.
* The **vector space** allows for semantic similarity comparison between tokens or texts.
* **Model weights** are learned parameters that guide model behavior.
* **Inference** is the process of using the model to generate or complete text.
* A **decoder** converts internal vector representations back into readable text.

You also explored:

* **Common applications** of language models:
  * Text generation
  * Semantic search
  * Chatbots
  * Summarization
  * Sentiment analysis
  * Moderation
  * Code generation


## Knowledge Check:
1. What does GPT stand for?
2. What is the difference between a Language Model (LM) and a Large Language Model (LLM)?
3. What is a token, and how is a sentence broken down into tokens?
4. What is the purpose of embeddings in natural language processing?
5. What is a vector in the context of text understanding?
6. Why is vector search used instead of keyword matching?
7. What is the role of FAISS in the system?
8. What kind of information is stored in MongoDB in this context?
---
# Section 2: Pre-requisites
This section tells you what **tools**, **skills**, and **basic setup** we should know or install before diving into tokens, embeddings, and vector search.

### Tools & Technologies we’ll Work With

Here’s a list of what we’ll use in this article — we don’t need to be an expert, but we should know **what each one does**.
```
 Python                  Main programming language we’ll use for writing code            
 pip                     Tool to install Python libraries (like a Play Store for Python) 
 OpenAI API              To get tokens and embeddings from models like GPT               
 FAISS                   To store and search vectors quickly                             
 MongoDB                 To store extra information (like text, title, date)             
 Token / tokenizer       To split text into tokens (words/subwords)                      
 NumPy                   To work with vectors and matrices (just number lists)          
 Requests                To call APIs like the News API                                  
```

### Software Requirements

Make sure you have these installed on your system:

```
# 1. Install Python (if not already installed)
python --version

# 2. Install pip (comes with Python >=3.6)
pip --version

# 3. Install required libraries
pip install openai faiss-cpu pymongo numpy requests 
```
If you’re using **Google Colab** or **Jupyter Notebook**, you can also install them inside a cell like this:

```
pip install openai faiss-cpu pymongo numpy requests tiktoken
```
Before diving deep into how tokens, embeddings, vectors, and tools like FAISS and MongoDB work together, let’s ensure we understand a few basic things. Don’t worry, this section is made super simple, like you’re learning from scratch.

You should be comfortable with:
1. Basic Python Programming
2. Understanding of Lists and Dictionaries
3. API (Application Programming Interface)
4. Vector (Basic Idea)
5. Basic Installation using pip

### API Keys You’ll Need

Before we start coding:

- Get an **OpenAI API key**: [https://platform.openai.com/account/api-keys] for GPT 4  
- Get a **News API key**: [https://newsapi.org](https://newsapi.org)  

We’ll use these to get real embeddings and news articles later in the article.
### Recap 
In this section, you’ve:
- Learned about the tools and technologies used in this project — from Python to FAISS and MongoDB.
- Set up your software environment with the necessary packages using pip.
- Understood the basic concepts like APIs, vectors, and tokenizers that form the backbone of how AI models work.
- Collected the API keys (OpenAI and NewsAPI) that we’ll use in later sections for real-world data and model outputs.
## Knowledge Check: Pre-requisites

1. What command would you use to install a package?
2. What does FAISS help us do?  
3. What kind of data format does MongoDB store?  
4. What kind of data structure is used to store metadata?
5. What tool do we use to install Python libraries?  
6. What is the purpose of an API?
7. Which library helps us make web API calls like NewsAPI?  
---
# What are Tokens and Tokenization
It is one of the most important and fundamental concepts in language models: 
GPT-2 from HuggingFace.
## What is a Token?
Think of a token as a small chunk of text.
* It could be a word
* Or a part of a word (called a sub-word)
* Or even just a character in some cases.

Let’s take this sentence:
```
"Tell me how to bake a cake"
```
When we send this sentence to a language model, it first breaks it down:
```
Sentence → Words → Sub-Words → Characters
```
Step 1 : Words 
```
 ["Tell","me","how","to","bake","a","Cake"]
 ```
 Step 2 : Sub words
 Some words are broken into parts the model knows better.
 ```
 ["Te", "ll", "me", "how", "to", "ba", "ke", "a", "ca", "ke"]
 ```
 Step 3 : Characters
Every sub-word is made up of characters.
```
['T', 'e', 'l', 'l']
```
This process is called **Tokenization** — converting human language into tokens that a machine can understand.
### Why Do We Tokenize?
AI models don’t understand full words directly. Instead, they understand numbers. So:
- First, we **tokenize** the sentence.
- Then, we **convert tokens into numbers**.
- These numbers are passed to models like **GPT-2**.
### Example: Tokenizing Text with GPT-2 (HuggingFace Transformers)
Let’s see how to tokenize a sentence using the GPT-2 tokenizer.

#### Install Required Libraries
```
pip install transformers
```
**Example :**

```python
from transformers import GPT2Tokenizer

# Load the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Your sentence
text = "Tell me how to bake a cake"

# Tokenize the sentence
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens: ", tokens)
print("Token IDs: ", token_ids)
```
**Output:**
```
Tokens: ['Tell', ' me', ' how', ' to', ' bake', ' a', ' cake']
Token IDs: [11250, 502, 703, 466, 10040, 257, 12141]
```
GPT-2 uses a special tokenizer called Byte Pair Encoding (BPE) — it splits even a single word into sub-parts based on what it has seen during training.
### Overview on Tokens and Tokenization
In this section, you’ve learned:
- A token can be a word, sub-word, or even a single character.
- The process of tokenization breaks down human language into tokens that a machine can understand.
- Tokenization is essential because models don’t understand words — they understand numbers representing those tokens.
- You saw how tokenization works step-by-step:
    * Sentence → Words → Sub-Words → Characters
- You used GPT-2's tokenizer (via HuggingFace) to:
    * Split a sentence into tokens
- Convert tokens into numerical IDs
- You also learned that GPT-2 uses Byte Pair Encoding (BPE) to tokenize text based on common subword patterns.


### Knowledge Check: Tokenization
1. What is tokenization?
2. Why do we break sentences into smaller units?
3. Which tokenizer does GPT-2 use?
4. What do token IDs represent?
5. Can tokens be smaller than words?
---
# Understanding the Importance of Embeddings and Vectors

Now that we know how a sentence is broken down into **tokens**, let’s understand what happens after that.
### What are Embeddings?

Imagine you say:   “I love ice cream.”
A human instantly understands the meaning. But a machine? It needs numbers to understand anything!

So here’s what happens:
1. Tokens → Numbers (Token IDs) 
   These are just IDs like: `[72, 123, 456]`
2. Numbers → Meaningful Vectors* 
   This is done using **embeddings**.
### Lets cook the story

Think of tokens like ingredients:  
- “pizza”, “burger”, and “fries” are all food.  
- A model doesn’t just see the word “pizza”— it sees a vector (a list of numbers) that tells it:
  - Pizza is food 
  - Pizza is not a vehicle 
  - Pizza is similar to burger 

So embeddings = numbers that carry the meaning of the word.

### What is a Vector?
A vector is just a list of numbers that describes something.

**Example**:
"love" → [0.21, -0.67, 0.45, 0.90, ..., 0.13]

Each number in this vector tells the model something about the **context or meaning** of the word.

### Example: Get Embeddings using GPT-2

GPT-2 does not give embeddings directly. It outputs something called "last hidden states" — these are embeddings for each token in the input.

### Example : Getting Embeddings from GPT-2

```python
from transformers import GPT2Tokenizer, GPT2Model
import torch

# Load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

# Sentence
text = "I love ice cream"

# Tokenize and convert to tensor
inputs = tokenizer(text, return_tensors="pt")

# Pass through model
with torch.no_grad():
    outputs = model(**inputs)

# Extract embeddings (last hidden state)
# Shape: [batch, tokens, hidden_dim]
embeddings = outputs.last_hidden_state

print("Token-level Embedding Shape:", embeddings.shape)
```
### Notes:
- last_hidden_state: Each word/token gets a vector (size 768 in GPT-2).
- These vectors hold meaning, not just position or spelling.
###  Why Are Embeddings Useful?
1. They capture semantic meaning\
→ “Happy” and “joyful” will have similar embeddings.
2. They allow math on text\
→ You can compute similarity: “king - man + woman ≈ queen”
3. They enable vector search, clustering, classification, and more.

### Knowledge Check: Embeddings and Vectors
1. What is an embedding?
2. How is a vector different from a token?
3. Why are embeddings useful?
4. What do the numbers inside an embedding represent?
5. How can we get embeddings from GPT-2?

---
## Section 5: Practice on Embeddings and Vectors

**In this section, you’ll:**
- Understand how to generate embeddings using GPT-2, GPT-4, and Ada (text-embedding-ada-002)
- Learn to convert text into high-dimensional vectors
- See how to reuse the same embedding logic with other models like Falcon, LLaMA, Claude, etc.
- Prepare your vectors for use in search, similarity scoring, and retrieval
- Let’s put your knowledge into practice. You’ll learn how to convert text into vectors (embeddings) using different models and use these vectors for comparison or storage.

### Example 1: Using GPT-2 Embeddings via Transformers
GPT-2 doesn’t give embeddings out of the box — but you can get the last hidden state and average it to create a fixed-size embedding.
```python
from transformers import GPT2Tokenizer, GPT2Model
import torch
import numpy as np

# Load GPT2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

def get_mean_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # Take the mean of the last hidden states
    last_hidden_state = outputs.last_hidden_state.squeeze(0)
    return last_hidden_state.mean(dim=0).numpy()

# Sample usage
text = "AI is revolutionizing the world."
embedding_gpt2 = get_mean_embeddings(text)
print("Embedding shape (GPT-2):", embedding_gpt2.shape)
print("Embedding (first 5 values):", embedding_gpt2[:5])
```
**Output:**
```
Embedding shape (GPT-2): (768,)
Embedding (first 5 values): [ 0.012, -0.045, 0.021, 0.037, -0.016]
```
### Example 2: GPT-4 Embeddings Using OpenAI API

```python
iimport openai
openai.api_key = "your-api-key"

def get_mean_embeddings(text):
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response['data'][0]['embedding']

# Example
embedding = get_mean_embeddings("AI is changing everything.")
print("GPT-4 Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])
```
**Output:**
```
Embedding length : 1536
Embedding (first 5 values): [-0.0103, 0.0217, -0.0184, 0.0325, -0.0051]
```
### Lets compare GPT2 Vs GPT4
| Model           | Vector Size | Comments                                 |
| --------------- | ----------- | ---------------------------------------- |
| GPT-2           | 768         | Uses hidden states, no direct embeddings |
| GPT-4 (via API) | 1536        | High-quality semantic embeddings         |

### Ada: Fast & Cost-Effective Embedding with text-embedding-ada-002
```python
def get_mean_embeddings(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

# Example
embedding = get_mean_embeddings("AI is changing everything.")
print("Ada Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])
```
**Output:**
```
Ada Embedding length: 1536
First 5 values: [-0.011, 0.027, -0.017, 0.036, -0.002]
```

### Can We Use Other Models?
| Model                   | How to Use                                | Library / API                  |
| ----------------------- | ----------------------------------------- | ------------------------------ |
| **Falcon**              | Use `AutoModel` from HuggingFace          | `transformers`                 |
| **LLaMA 2**             | Load with `transformers` & `bitsandbytes` | Meta (with license)            |
| **Claude AI**           | API-based via Anthropic                   | Anthropic SDK                  |
| **Gemini / Gemini Pro** | Google Cloud API                          | PaLM/Gemini embedding endpoint |

**Tip**: Any model that gives last hidden states or has a dedicated embedding endpoint can be used for vector search and similarity.

## Recap 
- You learned to extract embeddings from GPT-2, GPT-4 (3-small), and Ada
- GPT-2 requires custom pooling from hidden layers, while GPT-4 and Ada provide direct embeddings
- All OpenAI embeddings return 1536-dimensional vectors
- Many other models like LLaMA, Falcon, Claude, Gemini also support embedding workflows

## Knowledge Check
1. What is the output vector dimension from text-embedding-ada-002?
2. Which model needs you to compute the mean of hidden states?
3. Can GPT-4 give direct embeddings via the OpenAI API?
4. Name one model from HuggingFace that can be used to generate embeddings.
5. Is Ada model is more expensive than GPT-4 embedding model? Support your answer?

# Section 6: Importance of FAISS – Storing and Searching Vectors
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
# Section 7: Deep Dive into FAISS

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

