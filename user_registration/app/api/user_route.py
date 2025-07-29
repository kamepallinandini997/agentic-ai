from fastapi import APIRouter, HTTPException, Header
from app.models.schemas import ChangePassword, LoginUser, PasswordResetRequest, RegisterUser, ResetPassword
from app.services.user_service import change_user_password, handle_forgot_password, handle_reset_password, login_user, logout_user, register_user
from app.core.logging import logger

router = APIRouter()

@router.post("/register")
async def register(user: RegisterUser):
    try:
        logger.info("Called register function")
        result = await register_user(user)
        return result
    except Exception as e:
        logger.error(f"Registration failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/login")
async def login(user : LoginUser):
    try:
        logger.info("Called login function")
        result = await login_user(user)
        return result
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        raise HTTPException(status_code=500,detail=str(e))

@router.put("/change-password")
async def change_password(user : ChangePassword):
    try: 
        logger.info("calling change password ")
        result = await change_user_password(user)
        return result
    except Exception as e :
        logger.error(f"Change Password failed: {str(e)}")
        raise HTTPException(status_code= 500 , detail=str(e))
    
@router.post("/forgot-password")
async def forgot_password(data: PasswordResetRequest):
    try:
        result = await handle_forgot_password(data)
        return result
    except Exception as e:
        logger.error(f"Forgot Password failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-password")
async def reset_password(data: ResetPassword):
    try:
        result = await handle_reset_password(data)
        return result
    except Exception as e:
        logger.error(f"Reset password failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/logout")
async def logout(authorization: str = Header(...)):
    try:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token format")

        token = authorization.split(" ")[1]
        return await logout_user(token)
    
    except Exception as e:
       
        logger.error(f"Logout failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Something went wrong during logout")