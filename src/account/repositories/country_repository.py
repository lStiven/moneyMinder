from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.dtos import CountryDto
from src.account.models import Country
from src.base.repository import BaseRepository


class CountryRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, country_id: int) -> CountryDto:
        country = await self.get_by_id(Country, country_id)
        if country:
            return CountryDto.from_model(country)
        raise HTTPException(status_code=404, detail="Country not found")

    async def get_all(self) -> List[CountryDto]:
        result = await self.get_all_records(Country)
        return [CountryDto.from_model(record) for record in result]

    async def create(self, country: CountryDto) -> CountryDto:
        await self.country_validation(country)
        country_model: Country = country.to_model()
        record = await self.add_and_commit(country_model)
        return CountryDto.from_model(record)

    async def update(self, country_id: str, country: CountryDto) -> CountryDto:
        response = await self.get_by_id(Country, country_id)
        if response.code != country.code:
            self.country_validation(country)
        for key, value in country.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return CountryDto.from_model(response)

    async def delete(self, country_id: str) -> bool:
        country = await self.get_by_id(Country, country_id)
        if country:
            return await self.delete_record(country)
        raise HTTPException(status_code=404, detail="Country not found")

    async def get_by_code(self, code: str) -> CountryDto:
        country = await self.get_or_none(Country, code=code)
        return CountryDto.from_model(country) if country else None

    async def country_validation(self, country: CountryDto):
        existing_country = await self.get_by_code(country.code)
        if existing_country:
            raise HTTPException(status_code=400, detail="Country already exists")
