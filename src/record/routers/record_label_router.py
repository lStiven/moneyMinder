from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_record_label_service
from src.record.schemas.record_label_schema import RecordLabelSchema, RecordLabelSchemaResponse
from src.record.services import RecordLabelService

record_label_router = APIRouter(tags=["RecordLabel"], dependencies=[Depends(get_current_user)])


@record_label_router.get("/record_label", response_model=List[RecordLabelSchemaResponse])
async def get_all_record_labels(service: RecordLabelService = Depends(get_record_label_service)) -> List[dict]:
    return await service.get_all_record_labels()


@record_label_router.get("/record_label/{record_label_id}", response_model=RecordLabelSchemaResponse)
async def get_record_label(
    record_label_id: int, service: RecordLabelService = Depends(get_record_label_service)
) -> dict:
    return await service.get_record_label(record_label_id)


@record_label_router.post("/record_label", response_model=RecordLabelSchemaResponse)
async def create_record_label(
    record_label: RecordLabelSchema, service: RecordLabelService = Depends(get_record_label_service)
) -> dict:
    return await service.create_record_label(record_label)


@record_label_router.put("/record_label/{record_label_id}", response_model=RecordLabelSchemaResponse)
async def update_record_label(
    record_label_id: int,
    record_label: RecordLabelSchema,
    service: RecordLabelService = Depends(get_record_label_service),
) -> dict:
    return await service.update_record_label(record_label_id, record_label)


@record_label_router.delete("/record_label/{record_label_id}")
async def delete_record_label(
    record_label_id: int, service: RecordLabelService = Depends(get_record_label_service)
) -> bool:
    return await service.delete_record_label(record_label_id)
