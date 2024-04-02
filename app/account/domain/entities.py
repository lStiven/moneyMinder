

from app.account.application.dtos import (AccountDto, AccountTypeDTO,
                                          CountryDto, CurrencyDto)
from app.utils.base_entity import BaseEntity


class Country(BaseEntity):
    def __init__(self, id: str, name: str, code: str):
        super().__init__(id)
        self.name = name
        self.code = code
    
    @classmethod
    def from_dto(cls, dto: CountryDto):
        return cls(
            id=dto.id,
            name=dto.name,
            code=dto.code
        )
        
    def to_dto(self):
        return CountryDto(
            id=self.id,
            name=self.name,
            code=self.code           
        )
        
    def to_dict(self):
        return self.__dict__
        
        
class Currency(BaseEntity):
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        symbol: str,
        country: Country,
        exchange_rate: float,
        is_default: bool
    ):
        super().__init__(id)
        self.name = name
        self.code = code
        self.symbol = symbol
        self.country = country
        self.exchange_rate = exchange_rate
        self.is_default = is_default
    
    @classmethod
    def from_dto(cls, dto: CurrencyDto):
        return cls(
            id=dto.id,
            name=dto.name,
            code=dto.code,
            symbol=dto.symbol,
            country=Country.from_dto(dto.country),
            exchange_rate=dto.exchange_rate,
            is_default=dto.is_default
        )
        
    def to_dto(self):
        return CurrencyDto(
            id=self.id,
            name=self.name,
            code=self.code,
            symbol=self.symbol,
            country_id=self.country_id,
            exchange_rate=self.exchange_rate,
            is_default=self.is_default
        )
        
    def to_dict(self):
        return self.__dict__
    
    
    
    
    
class AccountType(BaseEntity):
    def __init__(self, id: str, name: str, code: str, icon: str):
        super().__init__(id)
        self.name = name
        self.code = code
        self.icon = icon
    
    @classmethod
    def from_dto(cls, dto: AccountTypeDTO):
        return cls(
            id=dto.id,
            name=dto.name,
            code=dto.code,
            icon=dto.icon
        )
        
    def to_dto(self):
        return AccountTypeDTO(
            id=self.id,
            name=self.name,
            code=self.code,    
            icon=self.icon,
        )
        
    def to_dict(self):
        return self.__dict__
    
    
class Account(BaseEntity):
    def __init__(self, id: str, name: str, code: str, account_type: AccountType, currency: Currency, initial_balance: float, balance: float, color: str, icon: str):
        super().__init__(id)
        self.name = name
        self.code = code
        self.account_type = account_type
        self.currency = currency
        self.initial_balance = initial_balance