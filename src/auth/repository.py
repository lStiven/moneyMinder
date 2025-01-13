from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from jose.exceptions import ExpiredSignatureError, JWTError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.constants import BEARER_TYPE, TOKEN_TYPE_ACCESS, TOKEN_TYPE_REFRESH
from src.auth.dto import RefreshTokenDto, TokenDto, UserDto
from src.auth.models import TokenRevoke, User
from src.auth.utils import create_access_token, decode_token, verify_password
from src.base.repository import BaseRepository
from src.logging_config import get_logger


class UserRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def login(self, email: str, password: str) -> TokenDto:
        try:
            user: Optional[User] = await self.get_or_none(User, email=email)
            if user is None or verify_password(password, user.hashed_password) is False:
                raise HTTPException(status_code=400, detail="Incorrect username or password")

            iat = datetime.now()
            user.last_login = iat
            user: User = await self.commit_and_refresh(user)
            access_token = create_access_token(data={"sub": user.email, "type": TOKEN_TYPE_ACCESS, "iat": iat})
            refresh_token = create_access_token(
                data={"sub": user.email, "type": TOKEN_TYPE_REFRESH, "iat": iat}, expires_delta=timedelta(days=1)
            )
            return TokenDto(access_token=access_token, refresh_token=refresh_token, token_type=BEARER_TYPE)
        except ExpiredSignatureError:
            raise HTTPException(status_code=400, detail="Token expired")
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def logout(self, token: str) -> bool:
        try:
            payload = decode_token(token)
            if payload["type"] != TOKEN_TYPE_ACCESS:
                return False
            user = await self.get_or_none(User, email=payload["sub"])
            if user is None:
                return False
            token_revoked = TokenRevoke(token=token, user_id=user.id)
            await self.add_and_commit(token_revoked)
            return True
        except ExpiredSignatureError:
            raise HTTPException(status_code=400, detail="Token expired")
        except JWTError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def refresh_token(self, token: str) -> RefreshTokenDto:
        try:
            payload = decode_token(token)
            if payload["type"] != TOKEN_TYPE_REFRESH:
                raise HTTPException(status_code=400, detail="Invalid token type")
            user = await self.get_or_none(User, email=payload["sub"])
            if user is None:
                raise HTTPException(status_code=400, detail="Invalid token")
            iat = datetime.now()
            access_token = create_access_token(data={"sub": user.email, "type": TOKEN_TYPE_ACCESS, "iat": iat})
            return RefreshTokenDto(access_token=access_token, token_type=BEARER_TYPE)
        except ExpiredSignatureError:
            raise HTTPException(status_code=400, detail="Token expired")
        except JWTError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def validate_token(self, token: str) -> UserDto:
        try:
            payload = decode_token(token)
            if payload["type"] != TOKEN_TYPE_ACCESS:
                raise HTTPException(status_code=400, detail="Invalid token type")
            user: User = await self.get_or_none(User, email=payload["sub"])
            if user is None:
                raise HTTPException(status_code=400, detail="Invalid token")
            revoked_token = await self.get_or_none(TokenRevoke, token=token, user_id=user.id)
            if revoked_token:
                raise HTTPException(status_code=400, detail="Invalid token")
            return UserDto.from_model(user)
        except HTTPException as e:
            raise e
        except ExpiredSignatureError as e:
            raise HTTPException(status_code=400, detail="Token expired")
        except JWTError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def create_user(self, user: UserDto) -> UserDto:
        try:
            user_model = user.to_model()
            return UserDto.from_model(await self.add_and_commit(user_model))
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
