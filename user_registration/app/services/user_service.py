from datetime import datetime, timedelta
import secrets
from fastapi import HTTPException
from app.db.mongo import users_collection,blacklist_collection
from app.models.schemas import ChangePassword, LoginUser, RegisterUser
from app.core.exceptions import validate_dates, validate_email_and_phone, validate_password_strength
from app.core.logging import logger
from app.utils.password_utils import hash_password, verify_password
from user_registration.app.utils.jwt_utils import generate_token

async def register_user(user_data: RegisterUser):
    user = user_data.dict()

    # Check if email and phone are not empty fields
    if not user["email"] or not user["phone"] or not user["password"]:
        logger.info("Email, phone number and password are missing")
        raise HTTPException(status_code=422, detail="Email, Phone number and Password are required.")

    # Check if email or phone number already exists
    await validate_email_and_phone(user["email"], user["phone"], users_collection)
    logger.info("Email and phone number are unique")

    # Validate password strength
    validate_password_strength(user["password"])
    logger.info("Password strength is good")
    user["password"] = hash_password(user["password"])

    # Validate DOB and DOJ
    if user["date_of_birth"] and user["date_of_joining"]:
        logger.info("Received date of birth and date of joining details")
        validate_dates(user["date_of_birth"], user["date_of_joining"])

    # Manipulate date format with time
    user["date_of_birth"] = datetime.combine(user["date_of_birth"], datetime.min.time())
    user["date_of_joining"] = datetime.combine(user["date_of_joining"], datetime.min.time())

    # Set user status as active
    user["status"] = "True"

    token = generate_token({"sub": user["email"] or user["phone"]})

    try:
        logger.info("Passed all requirements and saving to database")
        await users_collection.insert_one(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return {
        "status_code": 200,
        "message": "User registered successfully and You can login using your username",
        "token": token
    }

MAX_FAILED_ATTEMPTS = 5

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
        logger.info(f"User not found with {email_or_phone}")
        raise HTTPException(status_code=401, detail="User not found. Please sign up.")

    if user.get("account_locked", False):
        raise HTTPException(status_code=403, detail="Account is locked due to multiple failed login attempts. Please reset your password.")

    if not verify_password(input_password, user["password"]):
        logger.info("Invalid credentials")

        new_attempts = user.get("failed_login_attempts", 0) + 1
        updates = {
            "failed_login_attempts": new_attempts,
            "last_failed_login": datetime.utcnow()
        }

        if new_attempts >= MAX_FAILED_ATTEMPTS:
            updates["account_locked"] = True

        await users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": updates}
        )

        if updates.get("account_locked"):
            raise HTTPException(
                status_code=403,
                detail="Account locked after 5 failed attempts. Please reset your password."
            )
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    await users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {
            "failed_login_attempts": 0,
            "last_successful_login": datetime.utcnow()
        }}
    )

    token = generate_token({"sub": user["email"] or user["phone"]})

    return {
        "status_code": 200,
        "message": "Login successful",
        "token": token
    }

async def change_user_password(data: ChangePassword):
    if not data.email and not data.phone:
        raise HTTPException(status_code=422, detail="Email or phone number is required")

    user = await users_collection.find_one({
        "$or": [
            {"email": data.email},
            {"phone": data.phone}
        ]
    })

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if verify_password(data.new_password, user["password"]):
        raise HTTPException(status_code=400, detail="New password must be different from the old password")

    validate_password_strength(data.new_password)

    new_hashed = hash_password(data.new_password)
    await users_collection.update_one(
        {"email": data.email},
        {"$set": {"password": new_hashed}}
    )

    return {"status_code": 200, "message": "Password changed successfully"}

async def handle_forgot_password(data):
    if not data.email and not data.phone:
        raise HTTPException(status_code=400, detail="Email or phone number required.")

    query = {"$or": []}
    if data.email:
        query["$or"].append({"email": data.email})
    if data.phone:
        query["$or"].append({"phone": data.phone})

    user = await users_collection.find_one(query)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    token = secrets.token_urlsafe(32)
    expiry = datetime.utcnow() + timedelta(minutes=30)

    await users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"reset_token": token, "token_expiry": expiry}}
    )

    return {
        "message": "Use this reset token in the reset-password endpoint.",
        "reset_link": f"/auth/reset-password?token={token}",
        "expires_at": expiry.isoformat()
    }

async def handle_reset_password(data):
    user = await users_collection.find_one({"reset_token": data.token})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token.")

    if user["token_expiry"] < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Token has expired.")

    if verify_password(data.new_password, user["password"]):
        raise HTTPException(status_code=400, detail="New password must differ from old password.")

    hashed = hash_password(data.new_password)

    await users_collection.update_one(
        {"_id": user["_id"]},
        {
            "$set": {"password": hashed, "updated_at": datetime.utcnow()},
            "$unset": {"reset_token": "", "token_expiry": ""}
        }
    )

    return {"message": "Password updated successfully."}
async def logout_user(token: str):
    # Validate token format already checked in route
    try:
        payload = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    exp = payload.get("exp")
    if not exp:
        raise HTTPException(status_code=400, detail="No expiry found in token")

    await blacklist_collection.insert_one({
        "token": token,
        "expires_at": datetime.utcfromtimestamp(exp)
    })

    return {"message": "Logged out successfully"}
