from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class RecordLabelSchema(BaseModel):
    record_id: int = Field(..., title="Record ID", examples=[1, 2])
    label_id: int = Field(..., title="Label ID", examples=[1, 2])


class RecordLabelSchemaResponse(BaseSchema, RecordLabelSchema):
    pass
