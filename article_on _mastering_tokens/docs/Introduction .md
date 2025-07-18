# Introduction
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