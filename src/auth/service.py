from src.auth.dto import UserDto
from src.auth.repository import UserRepository
from src.auth.schemas import UserCreateSchema


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register(self, user: UserCreateSchema) -> dict:
        user_dto = await self.user_repository.create_user(UserDto.from_schema(user))
        return user_dto.to_dict()

    async def login(self, email: str, password: str) -> dict:
        token_dto = await self.user_repository.login(email, password)
        return token_dto.to_dict()

    async def logout(self, token: str) -> bool:
        return await self.user_repository.logout(token)

    async def refresh_token(self, token: str) -> dict:
        refresh_token_dto = await self.user_repository.refresh_token(token)
        return refresh_token_dto.to_dict()

    async def validate_token(self, token: str) -> dict:
        user_dto = await self.user_repository.validate_token(token)
        return user_dto.to_dict()
