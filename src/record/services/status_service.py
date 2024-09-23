from typing import List

from src.record.dtos import StatusDto
from src.record.repositories import StatusRepository
from src.record.schemas.status_schema import StatusSchema


class StatusService:
    def __init__(self, status_repository: StatusRepository):
        self.status_repository = status_repository

    async def get_status(self, status_id: int) -> dict:
        status_dto = await self.status_repository.get(status_id)
        return status_dto.to_dict() if status_dto else None

    async def get_all_statuss(self) -> List[dict]:
        statuss = await self.status_repository.get_all()
        return [status.to_dict() for status in statuss]

    async def create_status(self, status: StatusSchema) -> dict:
        status_dto = await self.status_repository.create(StatusDto.from_schema(status))
        return status_dto.to_dict()

    async def update_status(self, status_id: int, status: StatusSchema) -> dict:
        status_dto: StatusDto = await self.status_repository.update(status_id, StatusDto.from_schema(status))
        return status_dto.to_dict()

    async def delete_status(self, status_id: int) -> bool:
        return await self.status_repository.delete(status_id)
