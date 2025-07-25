from fastapi import HTTPException
from datetime import date
from app.core.logging import logger

import re

# Defining constants
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"

async def validate_email_and_phone(email : str ,phone : str,users_collection):
    """
    Validates if email or phone number already exists
    Takes input as three parameters
    Email : string
    Phone number : string and 
    collection : users_collection
    """
    existing_user = await users_collection.find_one({
        "$or":[
            {"email" : email},
            {"phone" : phone}
        ]
    })

    if existing_user :
        logger.info(f"Duplicate user found: {existing_user}")
        raise HTTPException(status_code= 400 ,
            detail="Email or phone number already exists. Try signing in or Use Forgot Password ")


def validate_password_strength(password: str):
    """
    Validates that the password meets the following:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if not re.match(PASSWORD_REGEX, password):
        raise HTTPException(
            status_code=422,
            detail=(
                "Password must be at least 8 characters long and contain at least one uppercase letter, "
                "one lowercase letter, one digit, and one special character."
            )
        )
    
def validate_dates(dob: date, doj: date):
    """
    Validates:
    - Date of joining should be after date of birth
    - Date of joining should not be in the future
    """
    today = date.today()
    if dob :
        if dob > today:
            raise HTTPException(
                status_code=400,
                detail="Date of Birth cannot be in future."
            )
    if doj:
        if doj < dob:
            raise HTTPException(
                status_code=400,
                detail="Date of Joining cannot be before Date of Birth."
            )
        if doj > today:
            raise HTTPException(
                status_code=400,
                detail="Date of Joining cannot be in the future."
            )