from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.dtos import CurrencyDto
from src.account.models import Currency
from src.base.repository import BaseRepository


class CurrencyRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, currency_id: int) -> CurrencyDto:
        currency = await self.get_by_id(Currency, currency_id)
        if currency:
            return CurrencyDto.from_model(currency)
        raise HTTPException(status_code=404, detail="Currency not found")

    async def get_all(self) -> List[CurrencyDto]:
        result = await self.get_all_records(Currency)
        return [CurrencyDto.from_model(record) for record in result]

    async def create(self, currency: CurrencyDto) -> CurrencyDto:
        try:
            await self.currency_validation(currency)
            currency_model: Currency = currency.to_model()
            record = await self.add_and_commit(currency_model)
            return CurrencyDto.from_model(record)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update(self, currency_id: int, currency: CurrencyDto) -> CurrencyDto:
        try:
            response = await self.get_by_id(Currency, currency_id)
            if not response:
                raise HTTPException(status_code=404, detail="Currency not found")
            if response.code != currency.code:
                self.currency_validation(currency)
            for key, value in currency.to_dict().items():
                if value:
                    setattr(response, key, value)
            response.updated_at = datetime.now()
            await self.commit_and_refresh(response)
            return CurrencyDto.from_model(response)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def delete(self, currency_id: int) -> bool:
        currency = await self.get_by_id(Currency, currency_id)
        if currency:
            return await self.delete_record(currency)
        raise HTTPException(status_code=404, detail="Currency not found")

    async def get_by_code(self, code: str) -> CurrencyDto:
        currency = await self.get_or_none(Currency, code=code)
        return CurrencyDto.from_model(currency) if currency else None

    async def currency_validation(self, currency: CurrencyDto):
        existing_currency = await self.get_by_code(currency.code)
        if existing_currency:
            raise HTTPException(status_code=400, detail="Currency already exists")
