from datetime import datetime
from fastapi import HTTPException
from app.db.mongo import users_collection
from app.models.schemas import UserRegister

async def register_user(user_data : UserRegister):
    user =  user_data.dict()

    user["date_of_birth"] = datetime.combine(user["date_of_birth"], datetime.min.time())
    user["date_of_joining"] = datetime.combine(user["date_of_joining"], datetime.min.time())

    user["status"] = "True"
    
    try:
        await users_collection.insert_one(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return {"status_code": 200, "message": "User registered successfully"}
