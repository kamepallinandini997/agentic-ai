"""
Autonomous Horoscope Processing Agent using Langchain
- Download today's horoscopes for all 12 zodiac signs
- Rewords text
- Generates keywords
- Detects sentiment
- Creates  ashort summary
- Saves processed data to JSON
"""

#==========================
# Config / setting
#==========================
HOROSCOPE_API_URL = "https://ohmanda.com/api/horoscope/"
SIGNS =[
     "aquarius","aries","taurus", "gemini", "cancer","leo",
     "virgo",
     "libra","scorpio","sagittarius","capricorn","pisces"
]
OUTPUT_FILE ="processed_horoscopes.json"
processed_results =[]

#==========================
# Import LangChain Modulels for Agent Creation
#==========================

import requests
import json

from langchain_openai import ChatOpenAI                  # Call Open AI GPT LLM
from langchain.agents import initialize_agent ,Tool      # Init and Create the Agent
from langchain.memory import ConversationBufferMemory    # Memory allocation for an agent


#==========================
# Setup LLM - Open Ai -GPT-4
#==========================

llm =ChatOpenAI(
    model= "gpt-4",
    temperature = "0.3"
)


#==========================
# Tools
#   1. download_horoscopes
#   2. reword_Horoscopes
#   3. generate_keywords
#   4. detect_sentiment
#   5. create_summary
#   6. save_to_json
#==========================

# Tool 1 - download_horoscopes
def download_horoscopes(_: str)->str :
    for sign in SIGNS:
        url = "{HOROSCOPE_API_URL}{sign}"
        response = requests.get(url)
        if response.status_code == 200:
            processed_results.append(
                {
                    "sign": sign,
                    "original" : response.json(),
                    "reworded" : "",
                    "keywords" : "",
                    "sentiment" : "",
                    "summary": ""
                }
            )
    return f"Downloaded horoscopes for {len(processed_results)}zodiac signs"


# Tool 2 - reword_horoscopes
def reword_horoscopes(index :str) ->str:
    idx = int(index)
    original_horoscope = processed_results[idx]["original"]["horoscope"]
    prompt = f"Reword this horoscope in 2 - 3 sentences for clarity: \n\n{original_horoscope}"
    reworded =llm.invoke(prompt).content.strip()
    processed_results[idx]["reworded"] = reworded
    return reworded

# Tool 3 - generate_keywords

def generate_keywords(index :str) ->str:
    idx =int(index)
    original_horoscope = processed_results[idx]["original"]["keywords"]["horoscope"]
    prompt = f"extract 3-5 keywords from this horoscope: \n\n {original_horoscope}"
    keywords = llm.invoke(prompt)
    processed_results[idx]["keywords"] = keywords
    return keywords

# Tool 4 - detect_sentiment
def detect_sentiment(index :str)->str :
    idx =int(index)
    original_horoscope = processed_results[idx]["original"]["horoscope"]
    prompt = f"Is this horoscope overall Postive , Negative or Neutral? Respond with one word only : \n\n {original_horoscope}"
    sentiment = llm.invoke(prompt).content.strip()
    processed_results[idx]["sentiment"] = sentiment
    return sentiment

# Tool 5 create_summary
def create_summary(index :str)->str :
    idx =int(index)
    original_horoscope = processed_results[idx]["original"]["summary"]
    prompt = f"Summarize this horoscope in one short sentence"
    summary = llm.invoke(prompt).content.strip()
    processed_results[idx]["summary"] = summary
    return summary

# Tool 6 save_to_json

def save_to_json(_: str)-> str:
    with open(OUTPUT_FILE,"w",encoding="utf-8") as f :
        json.dump(processed_results,f ,ensure_ascii=False,indent=4)
        return f"saved {len(processed_results)} to the {OUTPUT_FILE}"
    
#==========================
# Register tool with langchain
#==========================
tools = [
    Tool(name = "Download Horoscopes", func=download_horoscopes,description="fetch today's horoscope for all 12 zodiac signs"),
    Tool(name = "Reword Horoscopes", func=reword_horoscopes,description="Reword the horoscope at the given numerical index"),
    Tool(name = "Generate Keywords", func=generate_keywords,description="Genertate keyword for the horoscope at given numeric index"),
    Tool(name = "Detect Sentiment", func=detect_sentiment,description="Detect sentiment for the horoscope at given numeric index"),
    Tool(name = "Create Summary", func=create_summary,description="Create a short summary for the horoscope at given numeric index"),
    Tool(name = "Save To Json", func=save_to_json,description="Save all processed results to the JSON")
]

#==========================
# Assign memory to conversational buffer memory
#==========================
memory = ConversationBufferMemory(
    memory_key = "chat_history",
    return_messages= True
)

#==========================
# Create Agent / Init Agent
#==========================
agent =initialize_agent(
    tools = tools,
    llm = llm,
    agent = "zero-short-react-description",
    memory = memory,
    verbose = True,
    max_iterations = True
)


#==========================
# Goal
#==========================
goal =f"""
First call "Download Horoscopes" exactly once
Then for each index (0 to {len(SIGNS)-1} )
    1. Call "Reword Horoscopes" with the index
    2. Call "Generate Keywords" with the index
    3. Call "Detect Sentiment" with the index
    4. Call "Create Summary" with the index
After all the horoscopes are processed ,call 'Save To Json'
When done,respond ONLY with : PROCESSING_COMPLETE
"""
agent.invoke(
    {"input" : goal},
    handle_parsing_errors = True
)

print("\n Horoscope agent execution completed")