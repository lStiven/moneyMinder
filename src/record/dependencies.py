from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.record.repositories import (
    CategoryRepository,
    LabelRepository,
    PaymentRepository,
    RecordLabelRepository,
    RecordRepository,
    StatusRepository,
    SubCategoryRepository,
)
from src.record.services import (
    CategoryService,
    LabelService,
    PaymentService,
    RecordLabelService,
    RecordService,
    StatusService,
    SubCategoryService,
)


async def get_category_repository(db_session: AsyncSession = Depends(get_session)) -> CategoryRepository:
    return CategoryRepository(db_session)


async def get_category_service(
    category_repository: CategoryRepository = Depends(get_category_repository),
) -> CategoryService:
    return CategoryService(category_repository)


async def get_label_repository(db_session: AsyncSession = Depends(get_session)) -> LabelRepository:
    return LabelRepository(db_session)


async def get_label_service(label_repository: LabelRepository = Depends(get_label_repository)):
    return LabelService(label_repository)


async def get_payment_repository(db_session: AsyncSession = Depends(get_session)) -> PaymentRepository:
    return PaymentRepository(db_session)


async def get_payment_service(payment_repository: PaymentRepository = Depends(get_payment_repository)):
    return PaymentService(payment_repository)


async def get_record_label_repository(db_session: AsyncSession = Depends(get_session)) -> RecordLabelRepository:
    return RecordLabelRepository(db_session)


async def get_record_label_service(
    record_label_repository: RecordLabelRepository = Depends(get_record_label_repository),
):
    return RecordLabelService(record_label_repository)


async def get_record_repository(db_session: AsyncSession = Depends(get_session)) -> RecordRepository:
    return RecordRepository(db_session)


async def get_record_service(record_repository: RecordRepository = Depends(get_record_repository)):
    return RecordService(record_repository)


async def get_status_repository(db_session: AsyncSession = Depends(get_session)) -> StatusRepository:
    return StatusRepository(db_session)


async def get_status_service(status_repository: StatusRepository = Depends(get_status_repository)):
    return StatusService(status_repository)


async def get_sub_category_repository(db_session: AsyncSession = Depends(get_session)) -> SubCategoryRepository:
    return SubCategoryRepository(db_session)


async def get_sub_category_service(
    sub_category_repository: SubCategoryRepository = Depends(get_sub_category_repository),
):
    return SubCategoryService(sub_category_repository)
