from typing import List

from src.record.dtos import SubCategoryDto
from src.record.repositories import SubCategoryRepository
from src.record.schemas.sub_category_schema import SubCategorySchema


class SubCategoryService:
    def __init__(self, sub_category_repository: SubCategoryRepository):
        self.sub_category_repository = sub_category_repository

    async def get_sub_category(self, sub_category_id: int) -> dict:
        sub_category_dto = await self.sub_category_repository.get(sub_category_id)
        return sub_category_dto.to_dict() if sub_category_dto else None

    async def get_all_sub_categorys(self) -> List[dict]:
        sub_categorys = await self.sub_category_repository.get_all()
        return [sub_category.to_dict() for sub_category in sub_categorys]

    async def create_sub_category(self, sub_category: SubCategorySchema) -> dict:
        sub_category_dto = await self.sub_category_repository.create(SubCategoryDto.from_schema(sub_category))
        return sub_category_dto.to_dict()

    async def update_sub_category(self, sub_category_id: int, sub_category: SubCategorySchema) -> dict:
        sub_category_dto: SubCategoryDto = await self.sub_category_repository.update(
            sub_category_id, SubCategoryDto.from_schema(sub_category)
        )
        return sub_category_dto.to_dict()

    async def delete_sub_category(self, sub_category_id: int) -> bool:
        return await self.sub_category_repository.delete(sub_category_id)
