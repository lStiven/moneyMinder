import os


class Config:
    DEBUG = False
    TESTING = False
    DB_NAME = os.getenv("DATABASE_NAME")
    DB_USER = os.getenv("DATABASE_USER")
    DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DB_HOST = os.getenv("DATABASE_HOST")
    DB_PORT = os.getenv("DATABASE_PORT")
