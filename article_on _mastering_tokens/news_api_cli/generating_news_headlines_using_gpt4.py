import os
import faiss
import json
import torch
import logging
import requests
import pymongo
import openai
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2Model

# Configs
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "fd5dd9059e6c423ab6d91ea447f2e72d"
QUERY = "bitcoin"
ARTICLE_COUNT = 1
HEADLINE_COUNT = 5

OPENAI_API_KEY = "your_openai_api_key"  # Replace this
openai.api_key = OPENAI_API_KEY

MONGO_URI = "mongodb+srv://<db_username>:<db_password>@resumestore.08fnipm.mongodb.net/" # Replace this
DB_NAME = "news_article_api"
COLLECTION_NAME = "news_headlines"

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load GPT-2 tokenizer & model for embeddings
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
emb_model = GPT2Model.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
emb_model.pad_token_id = emb_model.config.eos_token_id

def fetch_article():
    logging.info("Fetching article from NewsAPI...")
    response = requests.get(NEWS_API_URL, params={
        "apiKey": NEWS_API_KEY,
        "pageSize": ARTICLE_COUNT,
        "q": QUERY
    })
    response.raise_for_status()
    articles = response.json().get("articles", [])
    if not articles:
        raise ValueError("No articles found.")
    logging.info(f"Fetched 1 article.")
    a = articles[0]
    return f"{a.get('title', '')}. {a.get('description', '')}. {a.get('content', '')}".strip()

def get_mean_embedding(text: str) -> torch.Tensor:
    logging.debug(f"Embedding: {text[:40]}...")
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = emb_model(**tokens)
    return output.last_hidden_state.mean(dim=1)

def generate_headlines_with_gpt4(prompt: str, count: int = HEADLINE_COUNT) -> list[str]:
    logging.info("Calling GPT-4 to generate headline candidates...")
    system_msg = "You are a helpful assistant that writes concise, one-line news headlines."
    user_msg = f"Write {count} different, short, catchy one-line headlines for the following news article:\n\n{prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.7
    )

    text_output = response.choices[0].message["content"]
    logging.debug(f"GPT-4 raw output:\n{text_output}")

    # Extract headlines: expect either newline list or numbered
    lines = text_output.split("\n")
    headlines = [line.lstrip("0123456789. ").strip() for line in lines if line.strip()]
    logging.info(f"Extracted {len(headlines)} headlines.")
    return headlines[:count]

def store_in_mongodb(data: dict):
    logging.info("Inserting into MongoDB...")
    client = pymongo.MongoClient(MONGO_URI)
    collection = client[DB_NAME][COLLECTION_NAME]
    collection.insert_one(data)
    logging.info("Inserted document into MongoDB.")

def main():
    try:
        article_text = fetch_article()
    except Exception as e:
        logging.error(f"Error fetching article: {e}")
        return

    prompt = f"{article_text}"
    article_emb = get_mean_embedding(prompt)

    try:
        headlines = generate_headlines_with_gpt4(prompt)
    except Exception as e:
        logging.error(f"Error calling GPT-4: {e}")
        return

    scored = []
    emb_list = []

    for h in headlines:
        h_emb = get_mean_embedding(h)
        score = F.cosine_similarity(h_emb, article_emb).item()
        scored.append((h, score))
        emb_list.append(h_emb.squeeze().numpy())
        logging.debug(f"Headline: {h} | Score: {score:.4f}")

    scored.sort(key=lambda x: x[1], reverse=True)

    index = faiss.IndexFlatL2(768)
    index.add(torch.tensor(emb_list).numpy())

    print("\nTop Headlines:")
    for i, (text, score) in enumerate(scored, 1):
        print(f"{i} {text} ({score:.4f})")

    doc = {
        "article": article_text,
        "headlines": [{"text": h, "score": round(s, 4)} for h, s in scored]
    }
    store_in_mongodb(doc)

if __name__ == "__main__":
    main()
