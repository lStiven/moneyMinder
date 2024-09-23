from typing import List

from src.record.dtos import PaymentDto
from src.record.repositories import PaymentRepository
from src.record.schemas.payment_schema import PaymentSchema


class PaymentService:
    def __init__(self, payment_repository: PaymentRepository):
        self.payment_repository = payment_repository

    async def get_payment(self, payment_id: int) -> dict:
        payment_dto = await self.payment_repository.get(payment_id)
        return payment_dto.to_dict() if payment_dto else None

    async def get_all_payments(self) -> List[dict]:
        payments = await self.payment_repository.get_all()
        return [payment.to_dict() for payment in payments]

    async def create_payment(self, payment: PaymentSchema) -> dict:
        payment_dto = await self.payment_repository.create(PaymentDto.from_schema(payment))
        return payment_dto.to_dict()

    async def update_payment(self, payment_id: int, payment: PaymentSchema) -> dict:
        payment_dto: PaymentDto = await self.payment_repository.update(payment_id, PaymentDto.from_schema(payment))
        return payment_dto.to_dict()

    async def delete_payment(self, payment_id: int) -> bool:
        return await self.payment_repository.delete(payment_id)
