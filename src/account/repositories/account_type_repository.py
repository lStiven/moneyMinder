from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.dtos.account_type_dto import AccountTypeDto
from src.account.models.account_type_model import AccountTypeModel
from src.base.repository import BaseRepository


class AccountTypeRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, account_type_id: int) -> AccountTypeDto:
        account_type = await self.get_by_id(AccountTypeModel, account_type_id)
        if account_type:
            return AccountTypeDto.from_model(account_type)
        raise HTTPException(status_code=404, detail="Account Type not found")

    async def get_all(self) -> List[AccountTypeDto]:
        result = await self.get_all_records(AccountTypeModel)
        return [AccountTypeDto.from_model(record) for record in result]

    async def create(self, account_type: AccountTypeDto) -> AccountTypeDto:
        await self.account_type_validation(account_type)
        account_type_model: AccountTypeModel = account_type.to_model()
        record = await self.add_and_commit(account_type_model)
        return AccountTypeDto.from_model(record)

    async def update(self, account_type_id: str, account_type: AccountTypeDto) -> AccountTypeDto:
        response = await self.get_by_id(AccountTypeModel, account_type_id)
        if response.code != account_type.code:
            self.account_type_validation(account_type)
        for key, value in account_type.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return AccountTypeDto.from_model(response)

    async def delete(self, account_type_id: str) -> bool:
        account_type = await self.get_by_id(AccountTypeModel, account_type_id)
        if account_type:
            return await self.delete_record(account_type)
        raise HTTPException(status_code=404, detail="Account Type not found")

    async def get_by_code(self, code: str) -> AccountTypeDto:
        account_type = await self.get_or_none(AccountTypeModel, code=code)
        return AccountTypeDto.from_model(account_type) if account_type else None

    async def account_type_validation(self, account_type: AccountTypeDto):
        existing_account_type = await self.get_by_code(account_type.code)
        if existing_account_type:
            raise HTTPException(status_code=400, detail="Account type already exists")
