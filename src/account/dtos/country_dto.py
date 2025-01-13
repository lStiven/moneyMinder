from dataclasses import dataclass

from src.account.models import Country
from src.account.schemas.country_schema import CountrySchema
from src.base.models import BaseDtoModel


@dataclass
class CountryDto(BaseDtoModel):
    name: str
    code: str
    phone_code: str

    @classmethod
    def from_schema(cls, schema: CountrySchema):
        return cls(
            id=None,
            name=schema.name,
            code=schema.code.upper(),
            phone_code=schema.phone_code,
            is_active=None,
            created_at=None,
            updated_at=None,
            created_by=None,
            updated_by=None,
        )

    @classmethod
    def from_model(cls, model: Country):
        return cls(
            id=model.id,
            name=model.name,
            code=model.code,
            phone_code=model.phone_code,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by,
            updated_by=model.updated_by,
        )

    def to_model(self) -> Country:
        return Country(
            id=self.id,
            name=self.name,
            code=self.code,
            phone_code=self.phone_code,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            created_by=self.created_by,
            updated_by=self.updated_by,
        )

    def to_dict(self):
        return self.__dict__
