from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from src.base.models import BaseModel
from src.record.constants import STATUS_TABLE_NAME


class Status(BaseModel):
    __tablename__ = STATUS_TABLE_NAME

    name: Mapped[str] = Column(String, nullable=False)
    code: Mapped[str] = Column(String, unique=True, nullable=False)
    color: Mapped[str] = Column(String, nullable=True)
