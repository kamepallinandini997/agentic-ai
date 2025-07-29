from jose import jwt
from datetime import datetime, timedelta

# Constants — move these to environment variables in production
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24  # token valid for 24 hours

def generate_token(payload: dict, expires_in: int = ACCESS_TOKEN_EXPIRE_HOURS) -> str:
    """
    Generate a JWT token with given payload and expiry (default 24 hours).
    """
    expire = datetime.utcnow() + timedelta(hours=expires_in)
    to_encode = payload.copy()
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

async def verify_token(token: str = Depends(oauth2_scheme)):
    # Check blacklist
    blacklisted = await blacklist_collection.find_one({"token": token})
    if blacklisted:
        raise HTTPException(status_code=401, detail="Token has been revoked")
    
    # Proceed with decoding
    return decode_token(token)
