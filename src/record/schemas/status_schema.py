from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class StatusSchema(BaseModel):
    name: str = Field(..., title="Status Name", examples=["Active", "Inactive"])
    code: str = Field(..., title="Status Code", examples=["ACTIVE", "INACTIVE"])
    color: Optional[str] = Field(..., title="Status Color", examples=["#000000", "#FFFFFF"])


class StatusSchemaResponse(BaseSchema, StatusSchema):
    pass
