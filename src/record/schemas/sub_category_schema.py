from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema
from src.record.schemas.category_schema import CategorySchema


class SubCategorySchema(BaseModel):
    name: str = Field(..., title="Sub Category Name", examples=["Food", "Transport"])
    code: str = Field(..., title="Sub Category Code", examples=["FOOD", "TRANSPORT"])
    icon: Optional[str] = Field(..., title="Sub Category Icon", examples=["icon.png"])
    category_id: int = Field(..., title="Category ID", examples=[1, 2])


class SubCategorySchemaResponse(BaseSchema, SubCategorySchema):
    category: Optional[CategorySchema]
