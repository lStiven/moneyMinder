from pydantic import BaseModel, Field
from src.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from dataclasses import dataclass
from typing import Optional


class BaseSchema(BaseModel):
    id: int = Field(..., title="ID", description="Unique identifier")
    created_at: datetime = Field(..., title="Created At", description="Creation date")
    updated_at: datetime = Field(..., title="Updated At", description="Last update date")
    created_by: Optional[str] = Field(None, title="Created By", description="User ID that created the record")
    updated_by: Optional[str] = Field(None, title="Updated By", description="User ID that updated the record")


@dataclass
class BaseDtoModel:
    id: int
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by = Column(String)
    updated_by = Column(String)
