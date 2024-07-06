from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class AccountTypeSchema(BaseModel):
    name: Optional[str] = Field(..., title="Account Type Name", example="Bank")
    code: Optional[str] = Field(..., title="Account Type Code", example="BANK")
    icon: Optional[str] = Field(
        ..., title="Account Type Icon", description="Icon base64 string", example="base64string"
    )


class AccountTypeSchemaResponse(BaseSchema, AccountTypeSchema):
    pass
