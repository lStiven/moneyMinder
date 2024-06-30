from pydantic import BaseModel, Field
from typing import Optional
from src.base.models import BaseSchema


class AccountTypeSchema(BaseModel):
    name: Optional[str] = Field(..., title="Account Type Name", example="Bank")
    code: Optional[str] = Field(..., title="Account Type Code", example="BANK")
    icon: Optional[str] = Field(
        ..., title="Account Type Icon", description="Icon base64 string", example="base64string"
    )


class AccountTypeSchemaResponse(BaseSchema, AccountTypeSchema):
    pass


class CountrySchema(BaseModel):
    name: str = Field(..., title="Country Name")
    code: str = Field(..., title="Country Code")


class CountrySchemaResponse(BaseSchema, CountrySchema):
    pass


class CurrencySchema(BaseModel):
    name: str = Field(..., title="Currency Name", example="United States Dollar")
    code: str = Field(..., title="Currency Code", example="USD")
    country_id: str = Field(..., title="Country ID")
    country: Optional[CountrySchema] = Field(None, title="Country")
    symbol: str = Field(..., title="Currency Symbol", example="$")
    exchange_rate: float = Field(..., title="Currency Exchange Rate", example=1.0)
    is_default: bool = Field(..., title="Is Default Currency", description="Is this currency the default currency?")


class CurrencySchemaResponse(BaseSchema, CurrencySchema):
    pass


class AccountSchema(BaseModel):
    name: str = Field(..., title="Account Name")
    code: str = Field(..., title="Account Code")
    account_type_id: str = Field(..., title="Account Type ID")
    account_type: Optional[AccountTypeSchema] = Field(None, title="Account Type")
    currency_id: str = Field(..., title="Currency ID")
    currency: Optional[CurrencySchema] = Field(None, title="Currency")
    innitial_balance: float = Field(
        ..., title="Initial Balance", description="Initial balance of the account", example=500.0
    )
    balance: float = Field(..., title="Balance", description="Current balance of the account", example=500.0)
    color: str = Field(..., title="Color", description="Color of the account", example="#000000")
    image: str = Field(..., title="Image", description="Image base64 string")

    class Config:
        schema_extra = {
            "example": {
                "name": "Bank Account",
                "code": "BANK_ACCOUNT",
                "account_type_id": "12345",
                "currency_id": "12345",
                "innitial_balance": 500.0,
                "balance": 500.0,
                "color": "#000000",
                "image": "base64string",
            }
        }
