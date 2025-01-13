from dataclasses import dataclass

from src.base.models import BaseDtoModel
from src.record.dtos.category_dto import CategoryDto
from src.record.models import SubCategory
from src.record.schemas.sub_category_schema import SubCategorySchema


@dataclass
class SubCategoryDto(BaseDtoModel):
    name: str
    code: str
    icon: str
    category_id: int
    category: CategoryDto = None

    @classmethod
    def from_schema(cls, schema: SubCategorySchema):
        return cls(
            id=None,
            name=schema.name,
            code=schema.code,
            icon=schema.icon,
            category_id=schema.category_id,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: SubCategory):
        return cls(
            id=model.id,
            name=model.name,
            code=model.code,
            icon=model.icon,
            category_id=model.category_id,
            category=CategoryDto.from_model(model.category) if model.category else None,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> SubCategory:
        return SubCategory(
            id=self.id,
            name=self.name,
            code=self.code.upper(),
            icon=self.icon,
            category_id=self.category_id,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "icon": self.icon,
            "category_id": self.category_id,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
            "category": self.category.to_dict() if self.category else None,
        }
