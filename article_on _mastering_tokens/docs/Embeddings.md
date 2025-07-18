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