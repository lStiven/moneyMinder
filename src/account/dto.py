from dataclasses import dataclass
from src.account.schemas import AccountTypeSchema
from src.account.models import AccountTypeModel
from uuid import uuid4


@dataclass
class AccountTypeDto:
    id: str
    name: str
    code: str
    icon: str

    @classmethod
    def from_schema(cls, schema: AccountTypeSchema):
        if schema.id is None:
            schema.id = str(uuid4())
        return cls(id=schema.id, name=schema.name, code=schema.code, icon=schema.icon)

    @classmethod
    def from_model(cls, model: AccountTypeModel):
        return cls(id=model.id, name=model.name, code=model.code, icon=model.icon)

    def to_schema(self) -> AccountTypeSchema:
        return AccountTypeSchema(id=self.id, name=self.name, code=self.code, icon=self.icon)

    def to_dict(self):
        return self.__dict__
