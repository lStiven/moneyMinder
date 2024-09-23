from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base.models import BaseModel
from src.record.constants import SUB_CATEGORY_TABLE_NAME


class SubCategory(BaseModel):
    __tablename__ = SUB_CATEGORY_TABLE_NAME

    name: Mapped[str] = Column(String, nullable=False)
    code: Mapped[str] = Column(String, unique=True, nullable=False)
    icon: Mapped[str] = Column(String, nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship("Category", lazy="selectin")
