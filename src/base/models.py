from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped

from src.database import Base


class BaseSchema(BaseModel):
    id: int = Field(..., title="ID", description="Unique identifier")
    is_active: bool = Field(..., title="Is Active", description="Record status")
    created_at: datetime = Field(..., title="Created At", description="Creation date")
    updated_at: datetime = Field(..., title="Updated At", description="Last update date")
    created_by: Optional[str] = Field(None, title="Created By", description="User ID that created the record")
    updated_by: Optional[str] = Field(None, title="Updated By", description="User ID that updated the record")


@dataclass
class BaseDtoModel:
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by: Mapped[str] = Column(String)
    updated_by: Mapped[str] = Column(String)
    is_active: Mapped[bool] = Column(Boolean, default=True)
