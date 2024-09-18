from dataclasses import dataclass

from src.auth.models import TokenRevoke, User
from src.auth.schemas import UserCreateSchema
from src.auth.utils import get_password_hash
from src.base.models import BaseDtoModel


@dataclass
class UserDto(BaseDtoModel):
    username: str
    email: str
    hashed_password: str
    is_superuser: bool

    @classmethod
    def from_schema(cls, schema: UserCreateSchema):
        return cls(
            id=None,
            username=schema.username,
            email=schema.email,
            hashed_password=get_password_hash(schema.password),
            is_superuser=schema.is_superuser,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: User):
        return cls(
            id=model.id,
            username=model.username,
            email=model.email,
            hashed_password=model.hashed_password,
            is_superuser=model.is_superuser,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_superuser=self.is_superuser,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": "",
            "is_superuser": self.is_superuser,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }


@dataclass
class TokenRevokeDto(BaseDtoModel):
    token: str
    revoked_at: str
    user_id: int

    @classmethod
    def from_model(cls, model: TokenRevoke):
        return cls(
            id=model.id,
            token=model.token,
            revoked_at=model.revoked_at,
            user_id=model.user_id,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> TokenRevoke:
        return TokenRevoke(
            id=self.id,
            token=self.token,
            revoked_at=self.revoked_at,
            user_id=self.user_id,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "token": self.token,
            "revoked_at": self.revoked_at,
            "user_id": self.user_id,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }


@dataclass
class TokenDto:
    access_token: str
    refresh_token: str
    token_type: str

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "token_type": self.token_type,
        }


@dataclass
class RefreshTokenDto:
    access_token: str
    token_type: str

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "token_type": self.token_type,
        }
