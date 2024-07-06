from typing import Optional

from pydantic import BaseModel, Field

from src.account.schemas.country_schema import CountrySchema
from src.base.models import BaseSchema


class CurrencySchema(BaseModel):
    name: str = Field(..., title="Currency Name", examples=["Peso", "Dollar"])
    code: str = Field(..., title="Currency Code", examples=["COP", "USD"])
    country_id: int = Field(..., title="Country ID", examples=[1, 2])
    symbol: str = Field(..., title="Currency Symbol", examples=["$", "€"])
    exchange_rate: float = Field(..., title="Currency Exchange Rate", examples=[1.0, 0.8])
    is_default: bool = Field(..., title="Currency Default", examples=[True, False])


class CurrencySchemaResponse(BaseSchema, CurrencySchema):
    country: Optional[CountrySchema]
