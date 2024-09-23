from sqlalchemy import Boolean, Column, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.account.constants import CURRENCY_TABLE_NAME
from src.base.models import BaseModel


class Currency(BaseModel):
    __tablename__ = CURRENCY_TABLE_NAME

    name: Mapped[str] = Column(String)
    code: Mapped[str] = Column(String, unique=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))
    symbol: Mapped[str] = Column(String)
    exchange_rate: Mapped[float] = Column(Float)
    is_default: Mapped[bool] = Column(Boolean)
    country: Mapped["Country"] = relationship("Country", back_populates="currencies", lazy="selectin")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "country": self.country.to_dict(),
            "symbol": self.symbol,
            "exchange_rate": self.exchange_rate,
            "is_default": self.is_default,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }
