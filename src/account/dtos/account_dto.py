from dataclasses import dataclass

from src.account.dtos.account_type_dto import AccountTypeDto
from src.account.dtos.currency_dto import CurrencyDto
from src.account.models import Account
from src.account.schemas.account_schema import AccountSchema
from src.base.models import BaseDtoModel


@dataclass
class AccountDto(BaseDtoModel):
    name: str
    account_type_id: int
    currency_id: int
    initial_balance: float
    balance: float
    color: str
    image: str
    currency: CurrencyDto = None
    account_type: AccountTypeDto = None

    @classmethod
    def from_schema(cls, schema: AccountSchema):
        return cls(
            id=None,
            name=schema.name,
            account_type_id=schema.account_type_id,
            currency_id=schema.currency_id,
            initial_balance=schema.initial_balance,
            balance=schema.balance,
            color=schema.color,
            image=schema.image,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: Account):
        return cls(
            id=model.id,
            name=model.name,
            account_type_id=model.account_type_id,
            currency_id=model.currency_id,
            initial_balance=model.initial_balance,
            balance=model.balance,
            color=model.color,
            image=model.image,
            currency=CurrencyDto.from_model(model.currency) if model.currency else None,
            account_type=AccountTypeDto.from_model(model.account_type) if model.account_type else None,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> Account:
        return Account(
            id=self.id,
            name=self.name,
            account_type_id=self.account_type_id,
            currency_id=self.currency_id,
            initial_balance=self.initial_balance,
            balance=self.balance,
            color=self.color,
            image=self.image,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )
