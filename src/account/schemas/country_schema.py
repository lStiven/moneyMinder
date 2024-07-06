from pydantic import BaseModel, Field

from src.base.models import BaseSchema


class CountrySchema(BaseModel):
    name: str = Field(..., title="Country Name", examples=["Colombia", "United States"])
    code: str = Field(..., title="Country Code", examples=["CO", "US"])
    phone_code: str = Field(..., title="Country Phone Code", examples=["57", "1"])


class CountrySchemaResponse(BaseSchema, CountrySchema):
    pass
