from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_record_service
from src.record.schemas.record_schema import RecordSchema, RecordSchemaResponse
from src.record.services import RecordService

record_router = APIRouter(tags=["Record"], dependencies=[Depends(get_current_user)])


@record_router.get("/record", response_model=List[RecordSchemaResponse])
async def get_all_records(service: RecordService = Depends(get_record_service)) -> List[dict]:
    return await service.get_all_records()


@record_router.get("/record/{record_id}", response_model=RecordSchemaResponse)
async def get_record(record_id: int, service: RecordService = Depends(get_record_service)) -> dict:
    return await service.get_record(record_id)


@record_router.post("/record", response_model=RecordSchemaResponse)
async def create_record(record: RecordSchema, service: RecordService = Depends(get_record_service)) -> dict:
    return await service.create_record(record)


@record_router.put("/record/{record_id}", response_model=RecordSchemaResponse)
async def update_record(
    record_id: int,
    record: RecordSchema,
    service: RecordService = Depends(get_record_service),
) -> dict:
    return await service.update_record(record_id, record)


@record_router.delete("/record/{record_id}")
async def delete_record(record_id: int, service: RecordService = Depends(get_record_service)) -> bool:
    return await service.delete_record(record_id)
