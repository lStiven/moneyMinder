from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class AccountTypeSchema(BaseModel):
    id: Optional[UUID] = Field(None, title="Account Type ID")
    name: str = Field(..., title="Account Type Name")
    code: str = Field(..., title="Account Type Code")
    icon: str = Field(..., title="Account Type Icon", description="Icon base64 string")


class CountrySchema(BaseModel):
    id: Optional[UUID] = Field(None, title="Country ID")
    name: str = Field(..., title="Country Name")
    code: str = Field(..., title="Country Code")


class CurrencySchema(BaseModel):
    id: Optional[UUID] = Field(None, title="Currency ID")
    name: str = Field(..., title="Currency Name", examples="United States Dollar")
    code: str = Field(..., title="Currency Code", examples="USD")
    country_id: str = Field(..., title="Country ID")
    country: Optional[CountrySchema] = Field(None, title="Country")
    symbol: str = Field(..., title="Currency Symbol", examples="$")
    exchange_rate: float = Field(..., title="Currency Exchange Rate", examples=1.0)
    is_default: bool = Field(..., title="Is Default Currency", description="Is this currency the default currency?")


class AccountSchema(BaseModel):
    id: Optional[UUID] = Field(None, title="Account ID")
    name: str = Field(..., title="Account Name")
    code: str = Field(..., title="Account Code")
    account_type_id: str = Field(..., title="Account Type ID")
    account_type: Optional[AccountTypeSchema] = Field(None, title="Account Type")
    currency_id: str = Field(..., title="Currency ID")
    currency: Optional[CurrencySchema] = Field(None, title="Currency")
    innitial_balance: float = Field(
        ..., title="Initial Balance", description="Initial balance of the account", examples=500.0
    )
    balance: float = Field(..., title="Balance", description="Current balance of the account", examples=500.0)
    color: str = Field(..., title="Color", description="Color of the account", examples="#000000")
    image: str = Field(..., title="Image", description="Image base64 string")
