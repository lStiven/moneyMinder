from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class PaymentSchema(BaseModel):
    name: str = Field(..., title="Payment Name", examples=["Cash", "Credit Card"])
    code: str = Field(..., title="Payment Code", examples=["CASH", "CC"])
    icon: Optional[str] = Field(..., title="Payment Icon", examples=["icon.png"])


class PaymentSchemaResponse(BaseSchema, PaymentSchema):
    pass
