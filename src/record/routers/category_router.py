from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_category_service
from src.record.schemas.category_schema import CategorySchema, CategorySchemaResponse
from src.record.services import CategoryService

category_router = APIRouter(tags=["Category"], dependencies=[Depends(get_current_user)])


@category_router.get("/category", response_model=List[CategorySchemaResponse])
async def get_all_categories(service: CategoryService = Depends(get_category_service)) -> List[dict]:
    return await service.get_all_categories()


@category_router.get("/category/{category_id}", response_model=CategorySchemaResponse)
async def get_category(category_id: int, service: CategoryService = Depends(get_category_service)) -> dict:
    return await service.get_category(category_id)


@category_router.post("/category", response_model=CategorySchemaResponse)
async def create_category(category: CategorySchema, service: CategoryService = Depends(get_category_service)) -> dict:
    return await service.create_category(category)


@category_router.put("/category/{category_id}", response_model=CategorySchemaResponse)
async def update_category(
    category_id: int,
    category: CategorySchema,
    service: CategoryService = Depends(get_category_service),
) -> dict:
    return await service.update_category(category_id, category)


@category_router.delete("/category/{category_id}")
async def delete_category(category_id: int, service: CategoryService = Depends(get_category_service)) -> bool:
    return await service.delete_category(category_id)
