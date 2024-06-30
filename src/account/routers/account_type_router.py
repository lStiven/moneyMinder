from typing import List

from fastapi import APIRouter, Depends

from src.account.dependencies import get_account_type_service
from src.account.schemas.account_type_schema import AccountTypeSchema, AccountTypeSchemaResponse
from src.account.services.account_type_service import AccountTypeService

account_type_router = APIRouter(tags=["Account Type"])


@account_type_router.get("/account_type", response_model=List[AccountTypeSchemaResponse])
async def get_all_account_types(service: AccountTypeService = Depends(get_account_type_service)) -> List[dict]:
    return await service.get_all_account_types()


@account_type_router.get("/account_type/{account_type_id}", response_model=AccountTypeSchemaResponse)
async def get_account_type(
    account_type_id: int, service: AccountTypeService = Depends(get_account_type_service)
) -> dict:
    return await service.get_account_type(account_type_id)


@account_type_router.post("/account_type", response_model=AccountTypeSchemaResponse)
async def create_account_type(
    account_type: AccountTypeSchema, service: AccountTypeService = Depends(get_account_type_service)
) -> dict:
    return await service.create_account_type(account_type)


@account_type_router.put("/account_type/{account_type_id}", response_model=AccountTypeSchemaResponse)
async def update_account_type(
    account_type_id: int,
    account_type: AccountTypeSchema,
    service: AccountTypeService = Depends(get_account_type_service),
) -> dict:
    return await service.update_account_type(account_type_id, account_type)


@account_type_router.delete("/account_type/{account_type_id}")
async def delete_account_type(
    account_type_id: int, service: AccountTypeService = Depends(get_account_type_service)
) -> bool:
    return await service.delete_account_type(account_type_id)
