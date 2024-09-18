from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.auth.repository import UserRepository
from src.auth.service import AuthService
from src.database import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_user_repository(db_session=Depends(get_session)) -> UserRepository:
    return UserRepository(db_session)


async def get_auth_service(user_repository=Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository)


async def get_current_user(
    token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    user = await auth_service.validate_token(token)
    return user
