from typing import List

from src.account.dtos import CountryDto
from src.account.repositories import CountryRepository
from src.account.schemas.country_schema import CountrySchema


class CountryService:
    def __init__(self, country_repository: CountryRepository):
        self.country_repository = country_repository

    async def get_country(self, country_id: str) -> dict:
        country_dto = await self.country_repository.get(country_id)
        return country_dto.to_dict() if country_dto else None

    async def get_all_countries(self) -> List[dict]:
        countries = await self.country_repository.get_all()
        return [country.to_dict() for country in countries]

    async def create_country(self, country: CountrySchema) -> dict:
        country_dto = await self.country_repository.create(CountryDto.from_schema(country))
        return country_dto.to_dict()

    async def update_country(self, country_id: str, country: CountrySchema) -> dict:
        country_dto: CountryDto = await self.country_repository.update(country_id, CountryDto.from_schema(country))
        return country_dto.to_dict()

    async def delete_country(self, country_id: str) -> bool:
        return await self.country_repository.delete(country_id)
