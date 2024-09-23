from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.record.dependencies import get_payment_service
from src.record.schemas.payment_schema import PaymentSchema, PaymentSchemaResponse
from src.record.services import PaymentService

payment_router = APIRouter(tags=["Payment"], dependencies=[Depends(get_current_user)])


@payment_router.get("/payment", response_model=List[PaymentSchemaResponse])
async def get_all_payments(service: PaymentService = Depends(get_payment_service)) -> List[dict]:
    return await service.get_all_payments()


@payment_router.get("/payment/{payment_id}", response_model=PaymentSchemaResponse)
async def get_payment(payment_id: int, service: PaymentService = Depends(get_payment_service)) -> dict:
    return await service.get_payment(payment_id)


@payment_router.post("/payment", response_model=PaymentSchemaResponse)
async def create_payment(payment: PaymentSchema, service: PaymentService = Depends(get_payment_service)) -> dict:
    return await service.create_payment(payment)


@payment_router.put("/payment/{payment_id}", response_model=PaymentSchemaResponse)
async def update_payment(
    payment_id: int,
    payment: PaymentSchema,
    service: PaymentService = Depends(get_payment_service),
) -> dict:
    return await service.update_payment(payment_id, payment)


@payment_router.delete("/payment/{payment_id}")
async def delete_payment(payment_id: int, service: PaymentService = Depends(get_payment_service)) -> bool:
    return await service.delete_payment(payment_id)
