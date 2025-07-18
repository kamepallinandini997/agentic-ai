# Section 3: What are Tokens and Tokenization
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
