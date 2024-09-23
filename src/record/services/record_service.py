from typing import List

from src.record.dtos import RecordDto
from src.record.repositories import RecordRepository
from src.record.schemas.record_schema import RecordSchema


class RecordService:
    def __init__(self, record_repository: RecordRepository):
        self.record_repository = record_repository

    async def get_record(self, record_id: int) -> dict:
        record_dto = await self.record_repository.get(record_id)
        return record_dto.to_dict() if record_dto else None

    async def get_all_records(self) -> List[dict]:
        records = await self.record_repository.get_all()
        return [record.to_dict() for record in records]

    async def create_record(self, record: RecordSchema) -> dict:
        record_dto = await self.record_repository.create(RecordDto.from_schema(record))
        return record_dto.to_dict()

    async def update_record(self, record_id: int, record: RecordSchema) -> dict:
        record_dto: RecordDto = await self.record_repository.update(record_id, RecordDto.from_schema(record))
        return record_dto.to_dict()

    async def delete_record(self, record_id: int) -> bool:
        return await self.record_repository.delete(record_id)
