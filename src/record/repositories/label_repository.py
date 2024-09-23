from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import LabelDto
from src.record.models import Label


class LabelRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, label_id: int) -> LabelDto:
        label = await self.get_by_id(Label, label_id)
        if label:
            return LabelDto.from_model(label)
        raise HTTPException(status_code=404, detail="Label not found")

    async def get_all(self) -> List[LabelDto]:
        result = await self.get_all_records(Label)
        return [LabelDto.from_model(record) for record in result]

    async def create(self, label: LabelDto) -> LabelDto:
        await self.label_validation(label)
        label_model: Label = label.to_model()
        record = await self.add_and_commit(label_model)
        return LabelDto.from_model(record)

    async def update(self, label_id: int, label: LabelDto) -> LabelDto:
        response = await self.get_by_id(Label, label_id)
        if not response:
            raise HTTPException(status_code=404, detail="Label not found")
        if response.code != label.code:
            self.label_validation(label)
        for key, value in label.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return LabelDto.from_model(response)

    async def delete(self, label_id: int) -> bool:
        label = await self.get_by_id(Label, label_id)
        if label:
            return await self.delete_record(label)
        raise HTTPException(status_code=404, detail="Label not found")

    async def get_by_code(self, code: str) -> LabelDto:
        label = await self.get_or_none(Label, code=code)
        return LabelDto.from_model(label) if label else None

    async def label_validation(self, label: LabelDto):
        existing_label = await self.get_by_code(label.code)
        if existing_label:
            raise HTTPException(status_code=400, detail="Label already exists")
