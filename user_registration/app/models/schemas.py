from pydantic import BaseModel ,EmailStr
from typing import Optional
from datetime import date

class RegisterUser(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: str
    password: str
    date_of_birth: date
    date_of_joining: Optional[date] = None
    address: Optional[str] = None
    comment: Optional[str] = None
    
class LoginUser(BaseModel):
    email_or_phone : str # Can be email or phone number
    password : str
