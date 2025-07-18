#  Pre-requisites
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