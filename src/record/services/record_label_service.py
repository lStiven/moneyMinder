from typing import List

from src.record.dtos import RecordLabelDto
from src.record.repositories import RecordLabelRepository
from src.record.schemas.record_label_schema import RecordLabelSchema


class RecordLabelService:
    def __init__(self, record_label_repository: RecordLabelRepository):
        self.record_label_repository = record_label_repository

    async def get_record_label(self, record_label_id: int) -> dict:
        record_label_dto = await self.record_label_repository.get(record_label_id)
        return record_label_dto.to_dict() if record_label_dto else None

    async def get_all_record_labels(self) -> List[dict]:
        record_labels = await self.record_label_repository.get_all()
        return [record_label.to_dict() for record_label in record_labels]

    async def create_record_label(self, record_label: RecordLabelSchema) -> dict:
        record_label_dto = await self.record_label_repository.create(RecordLabelDto.from_schema(record_label))
        return record_label_dto.to_dict()

    async def update_record_label(self, record_label_id: int, record_label: RecordLabelSchema) -> dict:
        record_label_dto: RecordLabelDto = await self.record_label_repository.update(
            record_label_id, RecordLabelDto.from_schema(record_label)
        )
        return record_label_dto.to_dict()

    async def delete_record_label(self, record_label_id: int) -> bool:
        return await self.record_label_repository.delete(record_label_id)
