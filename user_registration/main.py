from fastapi import FastAPI
from utils.logger import logger

app = FastAPI(
    title = "User Registration API",
    version = "1.0.0" 
)

@app.get("/health",tags = "Health")
def health_check():
    logger.info("Health endpoint called")
    return {"status" : "Healthy"}