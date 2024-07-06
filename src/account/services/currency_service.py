from typing import List

from src.account.dtos import CurrencyDto
from src.account.repositories import CurrencyRepository
from src.account.schemas.currency_schema import CurrencySchema


class CurrencyService:
    def __init__(self, currency_repository: CurrencyRepository):
        self.currency_repository = currency_repository

    async def get_currency(self, currency_id: str) -> dict:
        currency_dto = await self.currency_repository.get(currency_id)
        return currency_dto.to_dict() if currency_dto else None

    async def get_all_currencies(self) -> List[dict]:
        currencies = await self.currency_repository.get_all()
        return [currency.to_dict() for currency in currencies]

    async def create_currency(self, currency: CurrencySchema) -> dict:
        currency_dto = await self.currency_repository.create(CurrencyDto.from_schema(currency))
        return currency_dto.to_dict()

    async def update_currency(self, currency_id: str, currency: CurrencySchema) -> dict:
        currency_dto: CurrencyDto = await self.currency_repository.update(
            currency_id, CurrencyDto.from_schema(currency)
        )
        return currency_dto.to_dict()

    async def delete_currency(self, currency_id: str) -> bool:
        return await self.currency_repository.delete(currency_id)
