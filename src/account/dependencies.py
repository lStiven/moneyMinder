from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.repositories import AccountRepository, AccountTypeRepository, CountryRepository, CurrencyRepository
from src.account.services import AccountService, AccountTypeService, CountryService, CurrencyService
from src.database import get_session


async def get_account_type_repository(db_session: AsyncSession = Depends(get_session)) -> AccountTypeRepository:
    return AccountTypeRepository(db_session)


def get_account_type_service(
    account_type_repository: AccountTypeRepository = Depends(get_account_type_repository),
) -> AccountTypeService:
    return AccountTypeService(account_type_repository)


async def get_country_repository(db_session: AsyncSession = Depends(get_session)) -> CountryRepository:
    return CountryRepository(db_session)


def get_country_service(country_repository: CountryRepository = Depends(get_country_repository)):
    return CountryService(country_repository)


async def get_currency_repository(db_session: AsyncSession = Depends(get_session)) -> CurrencyRepository:
    return CurrencyRepository(db_session)


def get_currency_service(currency_repository: CurrencyRepository = Depends(get_currency_repository)):
    return CurrencyService(currency_repository)


def get_account_repository(db_session: AsyncSession = Depends(get_session)) -> AccountRepository:
    return AccountRepository(db_session)


async def get_account_service(account_repository: AccountRepository = Depends(get_account_repository)):
    return AccountService(account_repository)
