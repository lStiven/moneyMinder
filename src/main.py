from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.account.routers.account_type_router import account_type_router
from src.database import Base, engine
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
app.include_router(account_type_router)
