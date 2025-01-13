from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.account.routers import account_router, account_type_router, country_router, currency_router
from src.auth.router import auth_router
from src.record.routers import (
    category_router,
    label_router,
    payment_router,
    record_label_router,
    record_router,
    status_router,
    sub_category_router,
)

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(account_type_router)
app.include_router(country_router)
app.include_router(currency_router)
app.include_router(account_router)
app.include_router(category_router)
app.include_router(label_router)
app.include_router(payment_router)
app.include_router(record_label_router)
app.include_router(record_router)
app.include_router(status_router)
app.include_router(sub_category_router)
