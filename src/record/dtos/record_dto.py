from dataclasses import dataclass
from datetime import time as Time

from src.account.dtos.account_dto import AccountDto
from src.base.models import BaseDtoModel
from src.record.dtos.category_dto import CategoryDto
from src.record.dtos.payment_dto import PaymentDto
from src.record.dtos.status_dto import StatusDto
from src.record.models import Record
from src.record.models.record import RecordTypeEnum
from src.record.schemas.record_schema import RecordSchema


@dataclass
class RecordDto(BaseDtoModel):
    name: str
    amount: float
    record_type: RecordTypeEnum
    category_id: int
    account_id: int
    payee: str
    time: Time
    payment_id: int
    status_id: int
    latitude: float
    longitude: float
    attachment: str
    note: str
    category: CategoryDto = None
    account: AccountDto = None
    payment: PaymentDto = None
    status: StatusDto = None

    @classmethod
    def from_schema(cls, schema: RecordSchema):
        return cls(
            id=None,
            name=schema.name,
            amount=schema.amount,
            record_type=schema.record_type,
            category_id=schema.category_id,
            account_id=schema.account_id,
            payee=schema.payee,
            time=schema.time,
            payment_id=schema.payment_id,
            status_id=schema.status_id,
            latitude=schema.latitude,
            longitude=schema.longitude,
            attachment=schema.attachment,
            note=schema.note,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: Record):
        return cls(
            id=model.id,
            name=model.name,
            amount=model.amount,
            record_type=model.record_type.value,
            category_id=model.category_id,
            account_id=model.account_id,
            payee=model.payee,
            time=model.time,
            payment_id=model.payment_id,
            status_id=model.status_id,
            latitude=model.latitude,
            longitude=model.longitude,
            attachment=model.attachment,
            note=model.note,
            category=CategoryDto.from_model(model.category) if model.category else None,
            account=AccountDto.from_model(model.account) if model.account else None,
            payment=PaymentDto.from_model(model.payment) if model.payment else None,
            status=StatusDto.from_model(model.status) if model.status else None,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> Record:
        return Record(
            id=self.id,
            name=self.name,
            amount=self.amount,
            record_type=self.record_type.name,
            category_id=self.category_id,
            account_id=self.account_id,
            payee=self.payee,
            time=self.time,
            payment_id=self.payment_id,
            status_id=self.status_id,
            latitude=self.latitude,
            longitude=self.longitude,
            attachment=self.attachment,
            note=self.note,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "record_type": self.record_type,
            "category_id": self.category_id,
            "account_id": self.account_id,
            "payee": self.payee,
            "time": self.time,
            "payment_id": self.payment_id,
            "status_id": self.status_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "attachment": self.attachment,
            "note": self.note,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
            "category": self.category.to_dict() if self.category else None,
            "account": self.account.to_dict() if self.account else None,
            "payment": self.payment.to_dict() if self.payment else None,
            "status": self.status.to_dict() if self.status else None,
        }
