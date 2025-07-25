# Import necessary modules here
from fastapi import FastAPI
from app.api.user_route import router as user_router


# FastAPI Initialisation
app = FastAPI(
    title="User Registration",
    version= "1.0.0"
)

# Health check 
@app.get("/health-check")
def health_check():
    return {"Status":"Healthy"}

app.include_router(user_router, prefix="/user", tags=["User"])
