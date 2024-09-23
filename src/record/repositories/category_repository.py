from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import CategoryDto
from src.record.models import Category


class CategoryRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, category_id: int) -> CategoryDto:
        category = await self.get_by_id(Category, category_id)
        if category:
            return CategoryDto.from_model(category)
        raise HTTPException(status_code=404, detail="Category not found")

    async def get_all(self) -> List[CategoryDto]:
        result = await self.get_all_records(Category)
        return [CategoryDto.from_model(record) for record in result]

    async def create(self, category: CategoryDto) -> CategoryDto:
        await self.category_validation(category)
        category_model: Category = category.to_model()
        record = await self.add_and_commit(category_model)
        return CategoryDto.from_model(record)

    async def update(self, category_id: int, category: CategoryDto) -> CategoryDto:
        response = await self.get_by_id(Category, category_id)
        if not response:
            raise HTTPException(status_code=404, detail="Category not found")
        if response.code != category.code:
            self.category_validation(category)
        for key, value in category.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return CategoryDto.from_model(response)

    async def delete(self, category_id: int) -> bool:
        category = await self.get_by_id(Category, category_id)
        if category:
            return await self.delete_record(category)
        raise HTTPException(status_code=404, detail="Category not found")

    async def get_by_code(self, code: str) -> CategoryDto:
        category = await self.get_or_none(Category, code=code)
        return CategoryDto.from_model(category) if category else None

    async def category_validation(self, category: CategoryDto):
        existing_category = await self.get_by_code(category.code)
        if existing_category:
            raise HTTPException(status_code=400, detail="Category already exists")
