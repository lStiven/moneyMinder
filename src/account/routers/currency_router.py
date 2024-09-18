from typing import List

from fastapi import APIRouter, Depends

from src.account.dependencies import get_currency_service
from src.account.schemas.currency_schema import CurrencySchema, CurrencySchemaResponse
from src.account.services import CurrencyService
from src.auth.dependencies import get_current_user

currency_router = APIRouter(tags=["Currency"], dependencies=[Depends(get_current_user)])


@currency_router.get("/currency", response_model=List[CurrencySchemaResponse])
async def get_all_currencies(service: CurrencyService = Depends(get_currency_service)) -> List[dict]:
    return await service.get_all_currencies()


@currency_router.get("/currency/{currency_id}", response_model=CurrencySchemaResponse)
async def get_currency(currency_id: int, service: CurrencyService = Depends(get_currency_service)) -> dict:
    return await service.get_currency(currency_id)


@currency_router.post("/currency", response_model=CurrencySchemaResponse)
async def create_currency(currency: CurrencySchema, service: CurrencyService = Depends(get_currency_service)) -> dict:
    return await service.create_currency(currency)


@currency_router.put("/currency/{currency_id}", response_model=CurrencySchemaResponse)
async def update_currency(
    currency_id: int,
    currency: CurrencySchema,
    service: CurrencyService = Depends(get_currency_service),
) -> dict:
    return await service.update_currency(currency_id, currency)


@currency_router.delete("/currency/{currency_id}")
async def delete_currency(currency_id: int, service: CurrencyService = Depends(get_currency_service)) -> bool:
    return await service.delete_currency(currency_id)
