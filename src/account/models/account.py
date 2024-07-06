from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base.models import BaseModel
from src.constants import ACCOUNT_TABLE_NAME


class Account(BaseModel):
    __tablename__ = ACCOUNT_TABLE_NAME

    name: Mapped[str] = Column(String, index=True)
    account_type_id: Mapped[int] = mapped_column(ForeignKey("account_type.id"))
    curency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    initial_balance: Mapped[float] = Column(Float, default=0.0)
    balance: Mapped[float] = Column(Float, default=0.0)
    color: Mapped[str] = Column(String, default="#000000")
    image: Mapped[str] = Column(String, default="")
    currency: Mapped["Currency"] = relationship("Currency", lazy="selectin")
    account_type: Mapped["AccountType"] = relationship("AccountType", lazy="selectin")
