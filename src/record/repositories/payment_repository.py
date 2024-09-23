from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.repository import BaseRepository
from src.record.dtos import PaymentDto
from src.record.models import Payment


class PaymentRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)

    async def get(self, payment_id: int) -> PaymentDto:
        payment = await self.get_by_id(Payment, payment_id)
        if payment:
            return PaymentDto.from_model(payment)
        raise HTTPException(status_code=404, detail="Payment not found")

    async def get_all(self) -> List[PaymentDto]:
        result = await self.get_all_records(Payment)
        return [PaymentDto.from_model(record) for record in result]

    async def create(self, payment: PaymentDto) -> PaymentDto:
        await self.payment_validation(payment)
        payment_model: Payment = payment.to_model()
        record = await self.add_and_commit(payment_model)
        return PaymentDto.from_model(record)

    async def update(self, payment_id: int, payment: PaymentDto) -> PaymentDto:
        response = await self.get_by_id(Payment, payment_id)
        if not response:
            raise HTTPException(status_code=404, detail="Payment not found")
        if response.code != payment.code:
            self.payment_validation(payment)
        for key, value in payment.to_dict().items():
            if value:
                setattr(response, key, value)
        response.updated_at = datetime.now()
        await self.commit_and_refresh(response)
        return PaymentDto.from_model(response)

    async def delete(self, payment_id: int) -> bool:
        payment = await self.get_by_id(Payment, payment_id)
        if payment:
            return await self.delete_record(payment)
        raise HTTPException(status_code=404, detail="Payment not found")

    async def get_by_code(self, code: str) -> PaymentDto:
        payment = await self.get_or_none(Payment, code=code)
        return PaymentDto.from_model(payment) if payment else None

    async def payment_validation(self, payment: PaymentDto):
        existing_payment = await self.get_by_code(payment.code)
        if existing_payment:
            raise HTTPException(status_code=400, detail="Payment already exists")
