from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_label_service
from src.record.schemas.label_schema import LabelSchema, LabelSchemaResponse
from src.record.services import LabelService

label_router = APIRouter(tags=["Label"], dependencies=[Depends(get_current_user)])


@label_router.get("/label", response_model=List[LabelSchemaResponse])
async def get_all_labels(service: LabelService = Depends(get_label_service)) -> List[dict]:
    return await service.get_all_labels()


@label_router.get("/label/{label_id}", response_model=LabelSchemaResponse)
async def get_label(label_id: int, service: LabelService = Depends(get_label_service)) -> dict:
    return await service.get_label(label_id)


@label_router.post("/label", response_model=LabelSchemaResponse)
async def create_label(label: LabelSchema, service: LabelService = Depends(get_label_service)) -> dict:
    return await service.create_label(label)


@label_router.put("/label/{label_id}", response_model=LabelSchemaResponse)
async def update_label(
    label_id: int,
    label: LabelSchema,
    service: LabelService = Depends(get_label_service),
) -> dict:
    return await service.update_label(label_id, label)


@label_router.delete("/label/{label_id}")
async def delete_label(label_id: int, service: LabelService = Depends(get_label_service)) -> bool:
    return await service.delete_label(label_id)
