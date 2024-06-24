from injector import inject
from src.account.repository import AccountTypeRepository
from src.account.dto import AccountTypeDto
from typing import List


class AccountTypeService:
    @inject
    def __init__(self, account_type_repository: AccountTypeRepository):
        self.account_type_repository = account_type_repository

    async def get_account_type(self, account_type_id: str) -> dict:
        account_type_dto = await self.account_type_repository.get(account_type_id)
        return account_type_dto.to_dict() if account_type_dto else None

    async def create_account_type(self, account_type: dict) -> dict:
        account_type_dto = await self.account_type_repository.create(AccountTypeDto.from_schema(account_type))
        return account_type_dto.to_dict()

    async def get_all_account_types(self) -> List[dict]:
        account_types = await self.account_type_repository.get_all()
        return [account_type.to_dict() for account_type in account_types]
