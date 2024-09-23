from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import RecordDto
from src.record.models import Record


class RecordRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, record_id: int) -> RecordDto:
        record = await self.get_by_id(Record, record_id)
        if record:
            return RecordDto.from_model(record)
        raise HTTPException(status_code=404, detail="Record not found")

    async def get_all(self) -> List[RecordDto]:
        result = await self.get_all_records(Record)
        return [RecordDto.from_model(record) for record in result]

    async def create(self, record: RecordDto) -> RecordDto:
        try:
            record_model: Record = record.to_model()
            record = await self.add_and_commit(record_model)
            return RecordDto.from_model(record)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update(self, record_id: int, record: RecordDto) -> RecordDto:
        try:
            response = await self.get_by_id(Record, record_id)
            if not response:
                raise HTTPException(status_code=404, detail="Record not found")
            for key, value in record.to_dict().items():
                if value:
                    if key == "record_type":
                        value = value.name
                    setattr(response, key, value)
            response.updated_at = datetime.now()
            await self.commit_and_refresh(response)
            return RecordDto.from_model(response)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete(self, record_id: int) -> bool:
        record = await self.get_by_id(Record, record_id)
        if record:
            return await self.delete_record(record)
        raise HTTPException(status_code=404, detail="Record not found")
