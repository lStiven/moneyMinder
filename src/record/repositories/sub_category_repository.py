from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import SubCategoryDto
from src.record.models import SubCategory


class SubCategoryRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, sub_category_id: int) -> SubCategoryDto:
        sub_category = await self.get_by_id(SubCategory, sub_category_id)
        if sub_category:
            return SubCategoryDto.from_model(sub_category)
        raise HTTPException(status_code=404, detail="SubCategory not found")

    async def get_all(self) -> List[SubCategoryDto]:
        result = await self.get_all_records(SubCategory)
        return [SubCategoryDto.from_model(record) for record in result]

    async def create(self, sub_category: SubCategoryDto) -> SubCategoryDto:
        try:
            await self.sub_category_validation(sub_category)
            sub_category_model: SubCategory = sub_category.to_model()
            record = await self.add_and_commit(sub_category_model)
            return SubCategoryDto.from_model(record)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update(self, sub_category_id: int, sub_category: SubCategoryDto) -> SubCategoryDto:
        try:
            response = await self.get_by_id(SubCategory, sub_category_id)
            if not response:
                raise HTTPException(status_code=404, detail="SubCategory not found")
            if response.code != sub_category.code:
                self.sub_category_validation(sub_category)
            for key, value in sub_category.to_dict().items():
                if value:
                    setattr(response, key, value)
            response.updated_at = datetime.now()
            await self.commit_and_refresh(response)
            return SubCategoryDto.from_model(response)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete(self, sub_category_id: int) -> bool:
        sub_category = await self.get_by_id(SubCategory, sub_category_id)
        if sub_category:
            return await self.delete_record(sub_category)
        raise HTTPException(status_code=404, detail="SubCategory not found")

    async def get_by_code(self, code: str) -> SubCategoryDto:
        sub_category = await self.get_or_none(SubCategory, code=code)
        return SubCategoryDto.from_model(sub_category) if sub_category else None

    async def sub_category_validation(self, sub_category: SubCategoryDto):
        existing_sub_category = await self.get_by_code(sub_category.code)
        if existing_sub_category:
            raise HTTPException(status_code=400, detail="SubCategory already exists")
