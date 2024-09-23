import enum
from datetime import datetime

from sqlalchemy import Column, Float, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Enum

from src.base.models import BaseModel
from src.record.constants import RECORD_TABLE_NAME


class RecordTypeEnum(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class Record(BaseModel):
    __tablename__ = RECORD_TABLE_NAME

    name: Mapped[str] = Column(String, index=True)
    amount: Mapped[float] = Column(Float, nullable=False)
    record_type: Mapped[RecordTypeEnum] = Column(Enum(RecordTypeEnum), nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    payee: Mapped[str] = Column(String, nullable=True)
    time: Mapped[Time] = Column(Time, nullable=True, default=datetime.now().time())
    payment_id: Mapped[int] = mapped_column(ForeignKey("payment.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("status.id"))
    latitude: Mapped[float] = Column(Float, nullable=True)
    longitude: Mapped[float] = Column(Float, nullable=True)
    attachment: Mapped[str] = Column(String, nullable=True)
    note: Mapped[str] = Column(String, nullable=True)
    category: Mapped["Category"] = relationship("Category", lazy="selectin")
    account: Mapped["Account"] = relationship("Account", lazy="selectin")
    payment: Mapped["Payment"] = relationship("Payment", lazy="selectin")
    status: Mapped["Status"] = relationship("Status", lazy="selectin")
