from typing import List

from fastapi import APIRouter, Depends

from src.account.dependencies import get_account_service
from src.account.schemas.account_schema import AccountSchema, AccountSchemaResponse
from src.account.services import AccountService

account_router = APIRouter(tags=["Account"])


@account_router.get("/account", response_model=List[AccountSchemaResponse])
async def get_all_accounts(service: AccountService = Depends(get_account_service)) -> List[dict]:
    return await service.get_all_accounts()


@account_router.get("/account/{account_id}", response_model=AccountSchemaResponse)
async def get_account(account_id: str, service: AccountService = Depends(get_account_service)) -> dict:
    return await service.get_account(account_id)


@account_router.post("/account", response_model=AccountSchemaResponse)
async def create_account(account: AccountSchema, service: AccountService = Depends(get_account_service)) -> dict:
    return await service.create_account(account)


@account_router.put("/account/{account_id}", response_model=AccountSchemaResponse)
async def update_account(
    account_id: str,
    account: AccountSchema,
    service: AccountService = Depends(get_account_service),
) -> dict:
    return await service.update_account(account_id, account)


@account_router.delete("/account/{account_id}")
async def delete_account(account_id: str, service: AccountService = Depends(get_account_service)) -> bool:
    return await service.delete_account(account_id)
