from injector import Binder, Injector, Module, singleton
from src.config import Config as AppConfig
from src.config import Config
from src.gcp.client import DBInjector
from src.account.repository import AccountRepository, AccountTypeRepository, CurrencyRepository

Config.initialize_app()


class DependencyInjector(Module):
    def configure(self, binder: Binder) -> None:
        # binder.bind(storage.Client, to=storage.Client(), scope=singleton)
        binder.bind(DBInjector, to=DBInjector(), scope=singleton)
        binder.bind(AccountRepository, to=AccountRepository(AppConfig.ACCOUNT_TABLE_NAME, binder.injector.get(DBInjector)))
        binder.bind(AccountTypeRepository, to=AccountTypeRepository(AppConfig.ACCOUNT_TYPE_TABLE_NAME, binder.injector.get(DBInjector)))
        binder.bind(CurrencyRepository, to=CurrencyRepository(AppConfig.CURRENCY_TABLE_NAME, binder.injector.get(DBInjector)))
        binder.bind(CurrencyRepository, to=CurrencyRepository(AppConfig.CURRENCY_TABLE_NAME, binder.injector.get(DBInjector)))


injector = Injector([DependencyInjector()])
