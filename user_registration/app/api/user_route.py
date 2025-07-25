from fastapi import APIRouter, HTTPException
from app.models.schemas import UserRegister
from app.services.user_service import register_user

router = APIRouter()

@router.post("/register")
async def user_register(user: UserRegister):
    try:
        result = await register_user(user)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))