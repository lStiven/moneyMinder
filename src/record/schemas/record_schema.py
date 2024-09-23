import enum
from datetime import time as Time
from typing import Optional

from pydantic import BaseModel, Field

from src.account.schemas.account_schema import AccountSchema
from src.base.models import BaseSchema
from src.record.schemas.category_schema import CategorySchema
from src.record.schemas.payment_schema import PaymentSchema
from src.record.schemas.status_schema import StatusSchema


class RecordTypeEnum(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class RecordSchema(BaseModel):
    name: str = Field(..., title="Record Label Name", examples=["Groceries", "Utilities"])
    amount: float = Field(..., title="Record Label Amount", examples=[100.0, 200.0])
    record_type: RecordTypeEnum = Field(
        ...,
        title="Record Type",
        examples=["income", "expense", "transfer"],
        description="One of the following: income, expense, transfer",
    )
    category_id: int = Field(..., title="Category ID", examples=[1, 2])
    account_id: int = Field(..., title="Account ID", examples=[1, 2])
    payee: Optional[str] = Field(..., title="Record Label Payee", examples=["John Doe", "Jane Doe"])
    time: Optional[Time] = Field(..., title="Record Label Time", examples=["12:00:00", "13:00:00"])
    payment_id: int = Field(..., title="Payment ID", examples=[1, 2])
    status_id: int = Field(..., title="Status ID", examples=[1, 2])
    latitude: Optional[float] = Field(..., title="Record Label Latitude", examples=[-48.89])
    longitude: Optional[float] = Field(..., title="Record Label Longitude", examples=[-123.45])
    attachment: Optional[str] = Field(..., title="Record Label Attachment", examples=["attachment.png"])
    note: Optional[str] = Field(..., title="Record Label Note", examples=["Note 1", "Note 2"])


class RecordSchemaResponse(BaseSchema, RecordSchema):
    category: Optional[CategorySchema]
    account: Optional[AccountSchema]
    payment: Optional[PaymentSchema]
    status: Optional[StatusSchema]
