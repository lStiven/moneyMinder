from typing import List

from src.account.dtos.account_type_dto import AccountTypeDto
from src.account.repositories.account_type_repository import AccountTypeRepository
from src.account.schemas.account_type_schema import AccountTypeSchema


class AccountTypeService:
    def __init__(self, account_type_repository: AccountTypeRepository):
        self.account_type_repository = account_type_repository

    async def get_account_type(self, account_type_id: str) -> dict:
        account_type_dto = await self.account_type_repository.get(account_type_id)
        return account_type_dto.to_dict() if account_type_dto else None

    async def get_all_account_types(self) -> List[dict]:
        account_types = await self.account_type_repository.get_all()
        return [account_type.to_dict() for account_type in account_types]

    async def create_account_type(self, account_type: AccountTypeSchema) -> dict:
        account_type_dto = await self.account_type_repository.create(AccountTypeDto.from_schema(account_type))
        return account_type_dto.to_dict()

    async def update_account_type(self, account_type_id: str, account_type: AccountTypeSchema) -> dict:
        account_type_dto: AccountTypeDto = await self.account_type_repository.update(
            account_type_id, AccountTypeDto.from_schema(account_type)
        )
        return account_type_dto.to_dict()

    async def delete_account_type(self, account_type_id: str) -> bool:
        return await self.account_type_repository.delete(account_type_id)
