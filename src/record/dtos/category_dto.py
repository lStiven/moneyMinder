from dataclasses import dataclass

from src.base.models import BaseDtoModel
from src.record.models import Category
from src.record.schemas.category_schema import CategorySchema


@dataclass
class CategoryDto(BaseDtoModel):
    name: str
    code: str
    icon: str
    color: str

    @classmethod
    def from_schema(cls, schema: CategorySchema):
        return cls(
            id=None,
            name=schema.name,
            code=schema.code,
            icon=schema.icon,
            color=schema.color,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: Category):
        return cls(
            id=model.id,
            name=model.name,
            code=model.code,
            icon=model.icon,
            color=model.color,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> Category:
        return Category(
            id=self.id,
            name=self.name,
            code=self.code,
            icon=self.icon,
            color=self.color,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return self.__dict__
