import os
import faiss
import numpy as np
import fitz
from openai import OpenAI
from pymongo import MongoClient

#--------------------CONFIGURATIONS-------------------------

PDF_FOLDER = 'resumes'
FAISS_INDEX_FILE = 'resume_index.faiss'
INDEX_DATA_FILE  = 'resume_chunks,npy'
MONGO_URI ='mongodb+srv://kamepallinandini:<nandini0987>@resumestore.08fnipm.mongodb.net/'
DB_NAME = 'resume_manager'
COLLECTION_NAME ='resumes'
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
TEXT_EMBEDDINGs_MODEL = 'text-embedding-ada-002'

#--------------------INITIALIZATIONS-------------------------

openai_client = OpenAI(api_key= OPEN_API_KEY)
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
resume_collection = db[COLLECTION_NAME]
embedding_dim = 1536
index = faiss.IndexFlatL2(embedding_dim)
index_data = []


def load_pdf_text(pdf_path):
    pdf_document = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in pdf_document)

def chunk_text(text,chunk_size = 500):
    words = text.split()
    return  [" ".join(words[i: i+chunk_size]) for i in range(0,len(words),chunk_size)]

def get_openai_embeddings(text):
    response = openai_client.embeddings.create(
        model= TEXT_EMBEDDINGs_MODEL,
        input= text
    )
    return response.data[0].embedding

def save_index():
    faiss.write_index(index,FAISS_INDEX_FILE)
    np.save(INDEX_DATA_FILE,index_data) # Mapping 

def index_resume():
    global index_data
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            if resume_collection.find_one({"_id": filename}):
                print(f"Skipping : {filename} - already indexed")
                continue

            text = load_pdf_text(os.path.join(PDF_FOLDER,filename))
            chunks = chunk_text(text)
            for chunk in chunks:
                embedding = get_openai_embeddings(chunk)
                index.add(np.array(embedding, dtype = "float32"))
                index_data.append({"_id" : filename, "chunk" : chunk})
                resume_collection.insert_one({"_id" : filename, "text" : text})
            print(f"Indexed the resue {filename}")
    save_index()

def query_resume(query):
    return True


def main():
    while True:
        print("\n GP4 based resume QNA")
        print("1. Process the resumes in resume folder")
        print("2. Ask questions")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            index_resume()
        elif choice == "2":
            query = input("Ask your question: ")
            query_resume(query)
        elif choice == "3":
            print("Good Bye..... See you")
            break
        else:
            print("Invalid user input. Please try again")



if __name__ == "__main__":
    print("runniG MAIN FILE BUT IT IS MISSING OPEN AI " \
    "API KEY  FOR NOW NO NEED TO WORRY  WE WILL RUN IT " \
    "ONCE WHEN IT IS READY BEACUSE  ")
    main()