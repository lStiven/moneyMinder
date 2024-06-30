from dataclasses import dataclass
from src.account.schemas.account_type_schema import AccountTypeSchema
from src.account.models.account_type_model import AccountTypeModel
from datetime import datetime
from src.base.models import BaseDtoModel


@dataclass
class AccountTypeDto(BaseDtoModel):
    name: str
    code: str
    icon: str

    @classmethod
    def from_schema(cls, schema: AccountTypeSchema):
        return cls(
            id=None,
            name=schema.name,
            code=schema.code,
            icon=schema.icon,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: AccountTypeModel):
        return cls(
            id=model.id,
            name=model.name,
            code=model.code,
            icon=model.icon,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> AccountTypeModel:
        return AccountTypeModel(
            id=self.id,
            name=self.name,
            code=self.code,
            icon=self.icon,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return self.__dict__
