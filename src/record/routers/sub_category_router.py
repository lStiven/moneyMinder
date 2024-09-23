from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_sub_category_service
from src.record.schemas.sub_category_schema import SubCategorySchema, SubCategorySchemaResponse
from src.record.services import SubCategoryService

sub_category_router = APIRouter(tags=["SubCategory"], dependencies=[Depends(get_current_user)])


@sub_category_router.get("/sub_category", response_model=List[SubCategorySchemaResponse])
async def get_all_sub_categorys(service: SubCategoryService = Depends(get_sub_category_service)) -> List[dict]:
    return await service.get_all_sub_categorys()


@sub_category_router.get("/sub_category/{sub_category_id}", response_model=SubCategorySchemaResponse)
async def get_sub_category(
    sub_category_id: int, service: SubCategoryService = Depends(get_sub_category_service)
) -> dict:
    return await service.get_sub_category(sub_category_id)


@sub_category_router.post("/sub_category", response_model=SubCategorySchemaResponse)
async def create_sub_category(
    sub_category: SubCategorySchema, service: SubCategoryService = Depends(get_sub_category_service)
) -> dict:
    return await service.create_sub_category(sub_category)


@sub_category_router.put("/sub_category/{sub_category_id}", response_model=SubCategorySchemaResponse)
async def update_sub_category(
    sub_category_id: int,
    sub_category: SubCategorySchema,
    service: SubCategoryService = Depends(get_sub_category_service),
) -> dict:
    return await service.update_sub_category(sub_category_id, sub_category)


@sub_category_router.delete("/sub_category/{sub_category_id}")
async def delete_sub_category(
    sub_category_id: int, service: SubCategoryService = Depends(get_sub_category_service)
) -> bool:
    return await service.delete_sub_category(sub_category_id)
