from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.dtos import AccountDto
from src.account.models import Account
from src.base.repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, account_id: int) -> AccountDto:
        account = await self.get_by_id(Account, account_id)
        if account:
            return AccountDto.from_model(account)
        raise HTTPException(status_code=404, detail="Account not found")

    async def get_all(self) -> List[AccountDto]:
        result = await self.get_all_records(Account)
        return [AccountDto.from_model(record) for record in result]

    async def create(self, account: AccountDto) -> AccountDto:
        account_model: Account = account.to_model()
        record = await self.add_and_commit(account_model)
        return AccountDto.from_model(record)

    async def update(self, account_id: str, account: AccountDto) -> AccountDto:
        response = await self.get_by_id(Account, account_id)
        if response.code != account.code:
            self.account_validation(account)
        for key, value in account.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return AccountDto.from_model(response)

    async def delete(self, account_id: str) -> bool:
        account = await self.get_by_id(Account, account_id)
        if account:
            return await self.delete_record(account)
        raise HTTPException(status_code=404, detail="Account not found")

    async def get_by_code(self, code: str) -> AccountDto:
        account = await self.get_or_none(Account, code=code)
        return AccountDto.from_model(account) if account else None

    async def account_validation(self, account: AccountDto):
        existing_account = await self.get_by_code(account.code)
        if existing_account:
            raise HTTPException(status_code=400, detail="Account already exists")
