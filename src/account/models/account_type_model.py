from typing import Optional

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from src.base.models import BaseModel
from src.constants import ACCOUNT_TYPE_TABLE_NAME, COUNTRY_TABLE_NAME, CURRENCY_TABLE_NAME


class AccountTypeModel(BaseModel):
    __tablename__ = ACCOUNT_TYPE_TABLE_NAME

    name = Column(String)
    code = Column(String, unique=True)
    icon = Column(String, nullable=True)
    deleted = Column(Integer, default=0)

    @classmethod
    def from_sql_model(cls, sql_object: object):
        return cls(
            id=sql_object.id,
            name=sql_object.name,
            code=sql_object.code,
            icon=sql_object.icon,
            created_at=sql_object.created_at,
            updated_at=sql_object.updated_at,
            created_by=sql_object.created_by,
            updated_by=sql_object.updated_by,
        )

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


class CountryModel:
    def __init__(self, id: str, name: str, code: str):
        self.id = id
        self.name = name
        self.code = code

    @classmethod
    def from_gcp(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            code=data.get("code"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
        }


class CurrencyModel:
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        country: CountryModel,
        symbol: str,
        exchange_rate: float,
        is_default: bool,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.country = country
        self.symbol = symbol
        self.exchange_rate = exchange_rate
        self.is_default = is_default

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "country": self.country.to_dict(),
            "symbol": self.symbol,
            "exchange_rate": self.exchange_rate,
            "is_default": self.is_default,
        }


class AccountModel:
    def __init__(
        self,
        id: str,
        code: str,
        name: str,
        account_type: AccountTypeModel,
        currency: CurrencyModel,
        innitial_balance: float,
        balance: float,
        color: str,
        image: Optional[str] = None,
    ):
        self.id = id
        self.code = code
        self.name = name
        self.account_type = account_type
        self.currency = currency
        self.innitial_balance = innitial_balance
        self.balance = balance
        self.color = color
        self.image = image

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "account_type": self.account_type.to_dict(),
            "currency": self.currency.to_dict(),
            "innitial_balance": self.innitial_balance,
            "balance": self.balance,
            "color": self.color,
            "image": self.image,
        }
