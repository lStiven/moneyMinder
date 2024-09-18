from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.account.routers import account_router, account_type_router, country_router, currency_router
from src.auth.router import auth_router
from src.middleware import RateLimitingMiddleware

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Base.metadata.create_all(bind=engine)
# app.add_middleware(RateLimitingMiddleware)
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
