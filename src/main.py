from fastapi import FastAPI
from src.account.router import account_type_router

app = FastAPI()

app.include_router(account_type_router)
