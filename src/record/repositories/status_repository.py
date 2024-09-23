from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import StatusDto
from src.record.models import Status


class StatusRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, status_id: int) -> StatusDto:
        status = await self.get_by_id(Status, status_id)
        if status:
            return StatusDto.from_model(status)
        raise HTTPException(status_code=404, detail="Status not found")

    async def get_all(self) -> List[StatusDto]:
        result = await self.get_all_records(Status)
        return [StatusDto.from_model(record) for record in result]

    async def create(self, status: StatusDto) -> StatusDto:
        await self.status_validation(status)
        status_model: Status = status.to_model()
        record = await self.add_and_commit(status_model)
        return StatusDto.from_model(record)

    async def update(self, status_id: int, status: StatusDto) -> StatusDto:
        response = await self.get_by_id(Status, status_id)
        if not response:
            raise HTTPException(status_code=404, detail="Status not found")
        if response.code != status.code:
            self.status_validation(status)
        for key, value in status.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return StatusDto.from_model(response)

    async def delete(self, status_id: int) -> bool:
        status = await self.get_by_id(Status, status_id)
        if status:
            return await self.delete_record(status)
        raise HTTPException(status_code=404, detail="Status not found")

    async def get_by_code(self, code: str) -> StatusDto:
        status = await self.get_or_none(Status, code=code)
        return StatusDto.from_model(status) if status else None

    async def status_validation(self, status: StatusDto):
        existing_status = await self.get_by_code(status.code)
        if existing_status:
            raise HTTPException(status_code=400, detail="Status already exists")
