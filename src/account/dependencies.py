from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.repositories.account_type_repository import AccountTypeRepository
from src.account.services.account_type_service import AccountTypeService
from src.database import get_session


async def get_account_type_repository(db_session: AsyncSession = Depends(get_session)) -> AccountTypeRepository:
    return AccountTypeRepository(db_session)


def get_account_type_service(
    account_type_repository: AccountTypeRepository = Depends(get_account_type_repository),
) -> AccountTypeService:
    return AccountTypeService(account_type_repository)
