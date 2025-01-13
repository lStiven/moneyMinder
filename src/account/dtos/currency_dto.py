from dataclasses import dataclass

from src.account.dtos.country_dto import CountryDto
from src.account.models import Currency
from src.account.schemas.currency_schema import CurrencySchema
from src.base.models import BaseDtoModel


@dataclass
class CurrencyDto(BaseDtoModel):
    name: str
    code: str
    country_id: int
    symbol: str
    exchange_rate: float
    is_default: bool
    country: CountryDto = None

    @classmethod
    def from_schema(cls, schema: CurrencySchema):
        return cls(
            id=None,
            name=schema.name,
            code=schema.code.upper(),
            country_id=schema.country_id,
            symbol=schema.symbol,
            exchange_rate=schema.exchange_rate,
            is_default=schema.is_default,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: Currency):
        return cls(
            id=model.id,
            name=model.name,
            code=model.code,
            country_id=model.country_id,
            country=CountryDto.from_model(model.country) if model.country else None,
            symbol=model.symbol,
            exchange_rate=model.exchange_rate,
            is_default=model.is_default,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> Currency:
        return Currency(
            id=self.id,
            name=self.name,
            code=self.code,
            country_id=self.country_id,
            symbol=self.symbol,
            exchange_rate=self.exchange_rate,
            is_default=self.is_default,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "country_id": self.country_id,
            "symbol": self.symbol,
            "exchange_rate": self.exchange_rate,
            "is_default": self.is_default,
            "is_active": self.is_active,
            "country": self.country.to_dict() if self.country else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }
