from typing import Optional

from pydantic import BaseModel


class CountryDto(BaseModel):
    id: Optional[str]
    name: str
    code: str
    
    @classmethod
    def from_firebase(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            code=data.get('code')
        )
      
class CurrencyDto(BaseModel):
    id: Optional[str]
    name: str
    code: str
    symbol: str
    country_id: str
    country: Optional[CountryDto]
    exchange_rate: float
    is_default: bool
    

    
    @classmethod
    def from_firebase(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            code=data.get('code'),
            symbol=data.get('symbol'),
            country_id=data.get('country_id'),
            country=CountryDto.from_firebase(data.get('country')),
            exchange_rate=data.get('exchange_rate'),
            is_default=data.get('is_default')
        )


class AccountTypeDTO(BaseModel):
    id: Optional[str]
    name: str
    code: str
    icon: Optional[str]
    
    @classmethod
    def from_firebase(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            code=data.get('code'),
            icon=data.get('icon')
        )
    
    
class AccountDto(BaseModel):
    id: Optional[str]
    name: str
    code: str
    account_type_id: str
    account_type: Optional[AccountTypeDTO]
    currency_id: str
    currency: Optional[CurrencyDto]
    initial_balance: Optional[float]
    balance: Optional[float]
    color: Optional[str]
    icon: Optional[str]
    
    @classmethod
    def from_firebase(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            code=data.get('code'),
            account_type_id=data.get('account_type_id'),
            account_type=AccountTypeDTO.from_firebase(data.get('account_type')),
            currency_id=data.get('currency_id'),
            currency=CurrencyDto.from_firebase(data.get('currency')),
            initial_balance=data.get('initial_balance'),
            balance=data.get('balance'),
            color=data.get('color'),
            icon=data.get('icon')
        )