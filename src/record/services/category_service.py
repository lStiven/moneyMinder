from typing import List

from src.record.dtos import CategoryDto
from src.record.repositories import CategoryRepository
from src.record.schemas.category_schema import CategorySchema


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def get_category(self, category_id: int) -> dict:
        category_dto = await self.category_repository.get(category_id)
        return category_dto.to_dict() if category_dto else None

    async def get_all_categories(self) -> List[dict]:
        categories = await self.category_repository.get_all()
        return [category.to_dict() for category in categories]

    async def create_category(self, category: CategorySchema) -> dict:
        category_dto = await self.category_repository.create(CategoryDto.from_schema(category))
        return category_dto.to_dict()

    async def update_category(self, category_id: int, category: CategorySchema) -> dict:
        category_dto: CategoryDto = await self.category_repository.update(
            category_id, CategoryDto.from_schema(category)
        )
        return category_dto.to_dict()

    async def delete_category(self, category_id: int) -> bool:
        return await self.category_repository.delete(category_id)
