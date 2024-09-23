from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_status_service
from src.record.schemas.status_schema import StatusSchema, StatusSchemaResponse
from src.record.services import StatusService

status_router = APIRouter(tags=["Status"], dependencies=[Depends(get_current_user)])


@status_router.get("/status", response_model=List[StatusSchemaResponse])
async def get_all_statuss(service: StatusService = Depends(get_status_service)) -> List[dict]:
    return await service.get_all_statuss()


@status_router.get("/status/{status_id}", response_model=StatusSchemaResponse)
async def get_status(status_id: int, service: StatusService = Depends(get_status_service)) -> dict:
    return await service.get_status(status_id)


@status_router.post("/status", response_model=StatusSchemaResponse)
async def create_status(status: StatusSchema, service: StatusService = Depends(get_status_service)) -> dict:
    return await service.create_status(status)


@status_router.put("/status/{status_id}", response_model=StatusSchemaResponse)
async def update_status(
    status_id: int,
    status: StatusSchema,
    service: StatusService = Depends(get_status_service),
) -> dict:
    return await service.update_status(status_id, status)


@status_router.delete("/status/{status_id}")
async def delete_status(status_id: int, service: StatusService = Depends(get_status_service)) -> bool:
    return await service.delete_status(status_id)
