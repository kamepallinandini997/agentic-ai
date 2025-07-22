import logging
import requests
import torch
import faiss
import pymongo
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2LMHeadModel, GPT2Model

# Constants
NEWS_API_URL = "https://newsapi.org/v2/everything"
API_KEY = "fd5dd9059e6c423ab6d91ea447f2e72d"
QUERY = "bitcoin"
HEADLINE_COUNT = 5
ARTICLE_COUNT = 1
MONGO_URI = "mongodb+srv://<db_username>:<db_pasword>@resumestore.08fnipm.mongodb.net/" # update with your mongo credentials
DB_NAME = "news_article_api"
COLLECTION_NAME = "news_headlines"

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load Models
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
gen_model = GPT2LMHeadModel.from_pretrained("gpt2")
emb_model = GPT2Model.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token
gen_model.pad_token_id = gen_model.config.eos_token_id
emb_model.pad_token_id = emb_model.config.eos_token_id

def fetch_article():
    logging.info("Fetching news article from NewsAPI...")
    response = requests.get(NEWS_API_URL, params={
        "apiKey": API_KEY,
        "pageSize": ARTICLE_COUNT,
        "q": QUERY
    })
    response.raise_for_status()
    articles = response.json().get("articles", [])
    if not articles:
        raise ValueError("No articles found.")
    logging.info(f"Fetched {len(articles)} article(s) successfully.")
    a = articles[0]
    return f"{a.get('title', '')}. {a.get('description', '')}. {a.get('content', '')}".strip()

def get_mean_embedding(text: str) -> torch.Tensor:
    logging.debug(f"Generating embedding for text: {text[:50]}...")
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = emb_model(**tokens)
    return output.last_hidden_state.mean(dim=1)

def generate_headlines(prompt: str) -> list[str]:
    logging.info("Generating headline candidates using GPT-2...")
    tokens = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = gen_model.generate(
        tokens,
        num_return_sequences=HEADLINE_COUNT,
        max_new_tokens=20,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )
    headlines = [tokenizer.decode(out, skip_special_tokens=True).replace(prompt, "").strip() for out in outputs]
    cleaned = [h.split(".")[0].strip() for h in headlines if h.strip()]
    logging.info(f"Generated {len(cleaned)} headline candidates.")
    return cleaned

def store_in_mongodb(data: dict):
    logging.info("Connecting to MongoDB and inserting data...")
    client = pymongo.MongoClient(MONGO_URI)
    collection = client[DB_NAME][COLLECTION_NAME]
    collection.insert_one(data)
    logging.info("Data successfully inserted into MongoDB.")

def main():
    try:
        article_text = fetch_article()
    except Exception as e:
        logging.error(f"Failed to fetch article: {str(e)}")
        return

    logging.info("Creating prompt for headline generation...")
    prompt = f"Write a short, one-line headline for this news:\n{article_text}\nHeadline:"
    article_emb = get_mean_embedding(prompt)

    headlines = generate_headlines(prompt)
    if not headlines:
        logging.warning("No headlines generated. Exiting.")
        return

    scored = []
    emb_list = []
    logging.info("Scoring each generated headline using cosine similarity...")
    for h in headlines:
        h_emb = get_mean_embedding(h)
        score = F.cosine_similarity(h_emb, article_emb).item()
        scored.append((h, score))
        emb_list.append(h_emb.squeeze().numpy())
        logging.debug(f"Headline: '{h}' - Score: {score:.4f}")

    scored.sort(key=lambda x: x[1], reverse=True)

    # Add to FAISS (optional, illustration)
    logging.info("Adding headline embeddings to FAISS index...")
    index = faiss.IndexFlatL2(768)
    index.add(torch.tensor(emb_list).numpy())

    # Display top 5 headlines
    print("\nTop Headlines:")
    for i, (text, score) in enumerate(scored, 1):
        print(f"{i} {text} ({score:.4f})")

    # Prepare and insert into MongoDB
    result = {
        "article": article_text,
        "headlines": [{"text": h, "score": round(s, 4)} for h, s in scored]
    }
    store_in_mongodb(result)

if __name__ == "__main__":
    main()