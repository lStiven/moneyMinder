from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func

from src.auth.constants import TOKENS_REVOKE_TABLE_NAME, USER_TABLE_NAME
from src.base.models import BaseModel


class User(BaseModel):
    __tablename__ = USER_TABLE_NAME

    username: Mapped[str] = Column(String, unique=True)
    email: Mapped[str] = Column(String, unique=True)
    hashed_password: Mapped[str] = Column(String)
    is_superuser: Mapped[bool] = Column(Boolean, default=False)

    # accounts = relationship("Account", back_populates="user")


class TokenRevoke(BaseModel):
    __tablename__ = TOKENS_REVOKE_TABLE_NAME

    token: Mapped[str] = Column(String, unique=True, index=True)
    revoked_at: Mapped[datetime] = Column(DateTime, server_default=func.now())
    user_id: Mapped[int] = Column(Integer, ForeignKey(f"{USER_TABLE_NAME}.id"))
    user: Mapped["User"] = relationship("User", lazy="selectin")
