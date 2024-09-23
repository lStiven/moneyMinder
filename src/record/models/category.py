from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from src.base.models import BaseModel
from src.record.constants import CATEGORY_TABLE_NAME


class Category(BaseModel):
    __tablename__ = CATEGORY_TABLE_NAME

    name: Mapped[str] = Column(String, nullable=False)
    code: Mapped[str] = Column(String, unique=True, nullable=False)
    icon: Mapped[str] = Column(String, nullable=True)
    color: Mapped[str] = Column(String, nullable=True)
