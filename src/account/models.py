from typing import Optional


class AccountTypeModel:
    def __init__(self, id: str, name: str, code: str, icon: Optional[str] = None):
        self.id = id
        self.name = name
        self.code = code
        self.icon = icon

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "icon": self.icon,
        }


class CountryModel:
    def __init__(self, id: str, name: str, code: str):
        self.id = id
        self.name = name
        self.code = code

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
        }


class CurrencyModel:
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        country: CountryModel,
        symbol: str,
        exchange_rate: float,
        is_default: bool,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.country = country
        self.symbol = symbol
        self.exchange_rate = exchange_rate
        self.is_default = is_default

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "country": self.country.to_dict(),
            "symbol": self.symbol,
            "exchange_rate": self.exchange_rate,
            "is_default": self.is_default,
        }


class AccountModel:
    def __init__(
        self,
        id: str,
        code: str,
        name: str,
        account_type: AccountTypeModel,
        currency: CurrencyModel,
        innitial_balance: float,
        balance: float,
        color: str,
        image: Optional[str] = None,
    ):
        self.id = id
        self.code = code
        self.name = name
        self.account_type = account_type
        self.currency = currency
        self.innitial_balance = innitial_balance
        self.balance = balance
        self.color = color
        self.image = image

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "account_type": self.account_type.to_dict(),
            "currency": self.currency.to_dict(),
            "innitial_balance": self.innitial_balance,
            "balance": self.balance,
            "color": self.color,
            "image": self.image,
        }
