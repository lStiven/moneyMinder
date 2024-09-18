from typing import List

from src.account.dtos import AccountDto
from src.account.repositories import AccountRepository
from src.account.schemas.account_schema import AccountSchema


class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    async def get_account(self, account_id: int) -> dict:
        account_dto = await self.account_repository.get(account_id)
        return account_dto.to_dict() if account_dto else None

    async def get_all_accounts(self) -> List[dict]:
        accounts = await self.account_repository.get_all()
        return [account.to_dict() for account in accounts]

    async def create_account(self, account: AccountSchema) -> dict:
        account_dto = await self.account_repository.create(AccountDto.from_schema(account))
        return account_dto.to_dict()

    async def update_account(self, account_id: int, account: AccountSchema) -> dict:
        account_dto: AccountDto = await self.account_repository.update(account_id, AccountDto.from_schema(account))
        return account_dto.to_dict()

    async def delete_account(self, account_id: int) -> bool:
        return await self.account_repository.delete(account_id)
