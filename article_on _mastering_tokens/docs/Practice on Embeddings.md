# Practice on Embeddings and Vectors

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
