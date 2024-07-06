from typing import List

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from src.base.models import BaseModel
from src.constants import COUNTRY_TABLE_NAME


class Country(BaseModel):
    __tablename__ = COUNTRY_TABLE_NAME

    name: Mapped[str] = Column(String)
    code: Mapped[str] = Column(String, unique=True)
    phone_code: Mapped[str] = Column(String)
    currencies: Mapped[List["Currency"]] = relationship(
        back_populates="country", cascade="all, delete", lazy="selectin"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "phone_code": self.phone_code,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }
