from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from src.account.constants import ACCOUNT_TYPE_TABLE_NAME
from src.base.models import BaseModel


class AccountType(BaseModel):
    __tablename__ = ACCOUNT_TYPE_TABLE_NAME

    name: Mapped[str] = Column(String, nullable=False)
    code: Mapped[str] = Column(String, unique=True, nullable=False)
    icon: Mapped[str] = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "icon": self.icon,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }
