from fastapi import APIRouter
from src.account.schemas import AccountTypeSchema
from src.account.service import AccountTypeService
from src.dependency_injector import injector
from fastapi import HTTPException
from typing import List

account_type_router = APIRouter()


@account_type_router.get("/account_type/{account_type_id}", response_model=AccountTypeSchema)
async def get_account_type(account_type_id: str) -> AccountTypeSchema:
    account = await injector.get(AccountTypeService).get_account_type(account_type_id)
    if account:
        return account
    raise HTTPException(status_code=404, detail="Account type not found")


@account_type_router.post("/account_type", response_model=AccountTypeSchema)
async def create_account(account: AccountTypeSchema) -> AccountTypeSchema:
    return await injector.get(AccountTypeService).create_account_type(account)


@account_type_router.get("/account_type", response_model=List[AccountTypeSchema])
async def get_all_account_types() -> List[AccountTypeSchema]:
    return await injector.get(AccountTypeService).get_all_account_types()
