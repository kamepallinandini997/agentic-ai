from transformers import GPT2Tokenizer, GPT2Model
import torch
import torch.nn.functional as F

# Step 1: Read from text file
def read_article_and_headlines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("HEADLINES:")
    article = parts[0].replace("ARTICLE:", "").strip()
    headlines = [line.strip() for line in parts[1].strip().split('\n') if line.strip()]
    return article, headlines

# Step 2: Embedding function
def get_mean_embeddings(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state.mean(dim=1)

# Load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

# Step 3: Load data from file
article, headlines = read_article_and_headlines("input.txt")

# Step 4: Embed and compare
article_embedding = get_mean_embeddings(article)
results = []
for headline in headlines:
    headline_embedding = get_mean_embeddings(headline)
    score = F.cosine_similarity(article_embedding, headline_embedding).item()
    results.append((headline, score))

# Step 5: Sort and show
results.sort(key=lambda x: x[1], reverse=True)

# Top 4
print("\n Top 4 Similar Headlines:\n")
for i, (headline, score) in enumerate(results[:4], 1):
    print(f"{i}. {headline} - Score: {score:.4f}")

# All
print("\n All Headlines with Scores:\n")
for i, (headline, score) in enumerate(results, 1):
    print(f"{i}. {headline} - Score: {score:.4f}")
