from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.dependencies import get_auth_service, get_current_user
from src.auth.schemas import RefreshTokenSchema, TokenSchema, UserCreateSchema, UserSchema
from src.auth.service import AuthService

auth_router = APIRouter(tags=["Auth"])


@auth_router.post("/register", response_model=UserSchema)
async def register(user: UserCreateSchema, service: AuthService = Depends(get_auth_service)) -> dict:
    return await service.register(user)


@auth_router.post("/login", response_model=TokenSchema)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(get_auth_service)
) -> dict:
    return await service.login(form_data.username, form_data.password)


@auth_router.post("/logout")
async def logout(token: str, service: AuthService = Depends(get_auth_service)) -> bool:
    return await service.logout(token)


@auth_router.post("/refresh-token", response_model=RefreshTokenSchema, dependencies=[Depends(get_current_user)])
async def refresh_token(token: str, service: AuthService = Depends(get_auth_service)) -> dict:
    return await service.refresh_token(token)
