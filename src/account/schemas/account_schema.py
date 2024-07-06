from typing import Optional

from pydantic import BaseModel, Field

from src.account.schemas.currency_schema import CurrencySchema
from src.base.models import BaseSchema


class AccountSchema(BaseModel):
    name: str = Field(..., title="Account Name", examples=["Savings", "Checking"])
    account_type_id: int = Field(..., title="Account Type ID", examples=[1, 2])
    currency_id: int = Field(..., title="Currency ID", examples=[1, 2])
    balance: float = Field(..., title="Account Balance", examples=[100.0, 200.0])
    is_active: bool = Field(..., title="Account Active", examples=[True, False])
    color: str = Field(..., title="Account Color", examples=["#000000", "#FFFFFF"])
    image: str = Field(..., title="Account Image", examples=["", ""])


class AccountSchemaResponse(BaseSchema, AccountSchema):
    currency: Optional[CurrencySchema]
    # account_type: Optional[AccountTypeSchema]
