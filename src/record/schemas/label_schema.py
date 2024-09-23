from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class LabelSchema(BaseModel):
    name: str = Field(..., title="Label Name", examples=["Groceries", "Utilities"])
    code: str = Field(..., title="Label Code", examples=["GROCERIES", "UTILITIES"], description="Unique code for label")
    color: str = Field(..., title="Label Color", examples=["#000000", "#FFFFFF"])
    icon: Optional[str] = Field(..., title="Label Icon", examples=["icon.png"])


class LabelSchemaResponse(BaseSchema, LabelSchema):
    pass
