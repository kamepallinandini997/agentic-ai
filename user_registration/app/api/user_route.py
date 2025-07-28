from fastapi import APIRouter, HTTPException
from app.models.schemas import LoginUser, RegisterUser
from app.services.user_service import login_user, register_user
from app.core.logging import logger

router = APIRouter()

@router.post("/register")
async def register(user: RegisterUser):
    try:
        logger.info("Called register function")
        result = await register_user(user)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/login")
async def login(user : LoginUser):
    try:
        logger.info("Called login function")
        result = await login_user(user)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
