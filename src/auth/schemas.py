from pydantic import BaseModel, EmailStr

from src.base.models import BaseSchema


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreateSchema(UserBase):
    password: str
    is_superuser: bool


class UserSchema(BaseSchema, UserCreateSchema):
    pass

    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenSchema(BaseModel):
    access_token: str
    token_type: str
