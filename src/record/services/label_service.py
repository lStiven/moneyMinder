from typing import List

from src.record.dtos import LabelDto
from src.record.repositories import LabelRepository
from src.record.schemas.label_schema import LabelSchema


class LabelService:
    def __init__(self, label_repository: LabelRepository):
        self.label_repository = label_repository

    async def get_label(self, label_id: int) -> dict:
        label_dto = await self.label_repository.get(label_id)
        return label_dto.to_dict() if label_dto else None

    async def get_all_labels(self) -> List[dict]:
        labels = await self.label_repository.get_all()
        return [label.to_dict() for label in labels]

    async def create_label(self, label: LabelSchema) -> dict:
        label_dto = await self.label_repository.create(LabelDto.from_schema(label))
        return label_dto.to_dict()

    async def update_label(self, label_id: int, label: LabelSchema) -> dict:
        label_dto: LabelDto = await self.label_repository.update(label_id, LabelDto.from_schema(label))
        return label_dto.to_dict()

    async def delete_label(self, label_id: int) -> bool:
        return await self.label_repository.delete(label_id)
