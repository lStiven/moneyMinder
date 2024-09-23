from typing import Optional

from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class CategorySchema(BaseModel):
    name: str = Field(..., title="Category Name", examples=["Groceries", "Utilities"])
    code: str = Field(..., title="Category Code", examples=["GROCERIES", "UTILITIES"])
    color: Optional[str] = Field(..., title="Category Color", examples=["#000000", "#FFFFFF"])
    icon: Optional[str] = Field(..., title="Category Icon", examples=["icon.png"])


class CategorySchemaResponse(BaseSchema, CategorySchema):
    pass
