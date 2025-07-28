from datetime import datetime
from fastapi import HTTPException
from app.db.mongo import users_collection
from app.models.schemas import LoginUser, RegisterUser
from app.core.exceptions import validate_dates, validate_email_and_phone, validate_password_strength
from app.core.logging import logger
from app.utils.password_utils import hash_password, verify_password 


async def register_user(user_data : RegisterUser):
    user =  user_data.dict()
    # Validate email and phone existence
    if not user["email"] or not user["phone"] or not user["password"]:
        logger.info("Email, phone number and password are missing")
        raise HTTPException(status_code=422, detail="Email, Phone number and Password are required.")

    await validate_email_and_phone(user["email"], user["phone"], users_collection)

    # Validate password strength
    validate_password_strength(user["password"])
    user["password"] = hash_password(user["password"])

    # Validate DOB and DOJ
    if user["date_of_birth"]and user["date_of_joining"]:
        logger.info("Received date of birth and date and joining details proceeding with validation")
        validate_dates(user["date_of_birth"], user["date_of_joining"])

    user["date_of_birth"] = datetime.combine(user["date_of_birth"], datetime.min.time())
    user["date_of_joining"] = datetime.combine(user["date_of_joining"], datetime.min.time())

    user["status"] = "True"
    
    try:
        await users_collection.insert_one(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return {"status_code": 200, "message": "User registered successfully and You can login using your username"}


async def login_user(credentials: LoginUser):
    data = credentials.dict()
    email_or_phone = data["email_or_phone"]
    input_password = data["password"]

    user = await users_collection.find_one({
        "$or": [
            {"email": email_or_phone},
            {"phone": email_or_phone}
        ]
    })

    if not user:
        raise HTTPException(status_code=401, detail="User not found.Please Sign up ")

    if user.get("account_locked", False):
        raise HTTPException(status_code=403, detail="Account is locked. Please reset your password.")
    
    if not verify_password(input_password, user["password"]):
        # Log failed login attempt here
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"status_code": 200, "message": "Login successful"}





