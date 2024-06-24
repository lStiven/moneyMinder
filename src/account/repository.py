from typing import List
from src.gcp.client import DBInjector
from src.account.models import AccountModel, AccountTypeModel, CurrencyModel
from src.account.dto import AccountTypeDto


class AccountRepository:
    def __init__(self, table_name: str, db: DBInjector):
        self.client = db.client.collection(table_name)

    def get(self, account_id: str) -> AccountTypeDto:
        pass

    def get_all(self) -> List[AccountModel]:
        pass

    def create(self, account) -> AccountModel:
        self.client.document(account.id).set(account.to_dict())

    def get_by_code(self, code: str) -> AccountModel:
        pass

    def update(self, account: AccountModel) -> AccountModel:
        pass

    def delete(self, account_id: str) -> bool:
        pass


class AccountTypeRepository:

    def __init__(self, table_name: str, db: DBInjector):
        self.client = db.client.collection(table_name)

    async def get(self, account_type_id: str) -> AccountTypeDto:
        account_type = self.client.document(account_type_id).get()
        if account_type.exists:
            return AccountTypeDto.from_model(AccountTypeModel(**account_type.to_dict()))

    async def get_all(self) -> List[AccountTypeDto]:
        account_types = self.client.stream()
        return [AccountTypeDto.from_model(AccountTypeModel(**account.to_dict())) for account in account_types]

    async def create(self, account_type: AccountTypeDto) -> AccountTypeDto:
        self.client.document(account_type.id).set(account_type.to_dict())
        return account_type

    async def update(self, account_type: AccountTypeDto) -> AccountTypeDto:
        pass

    async def delete(self, account_type_id: str) -> bool:
        self.client.document(account_type_id).delete()
        return True


class CurrencyRepository:

    def __init__(self, table_name: str, db: DBInjector):
        self.client = db.client.collection(table_name)

    async def get(self, currency_id: str) -> CurrencyModel:
        pass

    async def get_all(self) -> List[CurrencyModel]:
        pass

    async def create(self, currency: CurrencyModel) -> CurrencyModel:
        pass

    async def update(self, currency: CurrencyModel) -> CurrencyModel:
        pass

    async def delete(self, currency_id: str) -> bool:
        pass
