import bcrypt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def generate_reset_token(user, users_collection):
    token = secrets.token_urlsafe(32)
    expiry = datetime.utcnow() + timedelta(minutes=30)

    await users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"reset_token": token, "token_expiry": expiry}}
    )

    return token, expiry

async def reset_password_with_token(data, users_collection):
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
