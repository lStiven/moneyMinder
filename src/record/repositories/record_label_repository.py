from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import RecordLabelDto
from src.record.models import RecordLabel


class RecordLabelRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, record_label_id: int) -> RecordLabelDto:
        record_label = await self.get_by_id(RecordLabel, record_label_id)
        if record_label:
            return RecordLabelDto.from_model(record_label)
        raise HTTPException(status_code=404, detail="RecordLabel not found")

    async def get_all(self) -> List[RecordLabelDto]:
        result = await self.get_all_records(RecordLabel)
        return [RecordLabelDto.from_model(record) for record in result]

    async def create(self, record_label: RecordLabelDto) -> RecordLabelDto:
        try:
            record_label_model: RecordLabel = record_label.to_model()
            record = await self.add_and_commit(record_label_model)
            return RecordLabelDto.from_model(record)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update(self, record_label_id: int, record_label: RecordLabelDto) -> RecordLabelDto:
        try:
            response = await self.get_by_id(RecordLabel, record_label_id)
            if not response:
                raise HTTPException(status_code=404, detail="RecordLabel not found")
            for key, value in record_label.to_dict().items():
                if value:
                    setattr(response, key, value)
            response.updated_at = datetime.now()
            await self.commit_and_refresh(response)
            return RecordLabelDto.from_model(response)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete(self, record_label_id: int) -> bool:
        record_label = await self.get_by_id(RecordLabel, record_label_id)
        if record_label:
            return await self.delete_record(record_label)
        raise HTTPException(status_code=404, detail="RecordLabel not found")
