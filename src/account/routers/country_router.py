from typing import List

from fastapi import APIRouter, Depends

from src.account.dependencies import get_country_service
from src.account.schemas.country_schema import CountrySchema, CountrySchemaResponse
from src.account.services import CountryService

country_router = APIRouter(tags=["Country"])


@country_router.get("/country", response_model=List[CountrySchemaResponse])
async def get_all_countries(service: CountryService = Depends(get_country_service)) -> List[dict]:
    return await service.get_all_countries()


@country_router.get("/country/{country_id}", response_model=CountrySchemaResponse)
async def get_country(country_id: int, service: CountryService = Depends(get_country_service)) -> dict:
    return await service.get_country(country_id)


@country_router.post("/country", response_model=CountrySchemaResponse)
async def create_country(country: CountrySchema, service: CountryService = Depends(get_country_service)) -> dict:
    return await service.create_country(country)


@country_router.put("/country/{country_id}", response_model=CountrySchemaResponse)
async def update_country(
    country_id: int,
    country: CountrySchema,
    service: CountryService = Depends(get_country_service),
) -> dict:
    return await service.update_country(country_id, country)


@country_router.delete("/country/{country_id}")
async def delete_country(country_id: int, service: CountryService = Depends(get_country_service)) -> bool:
    return await service.delete_country(country_id)
