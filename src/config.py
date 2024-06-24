import os
import firebase_admin
from firebase_admin import credentials


class Config:
    DEBUG = False
    TESTING = False
    FIREBASE_ADMIN_SDK = os.environ.get("FIREBASE_ADMIN_SDK")
    ACCOUNT_TABLE_NAME = "accounts"
    ACCOUNT_TYPE_TABLE_NAME = "account_types"
    CURRENCY_TABLE_NAME = "currencies"
    COUNTRY_TABLE_NAME = "countries"

    @classmethod
    def initialize_app(cls):
        try:
            cred = credentials.Certificate(cls.FIREBASE_ADMIN_SDK)
            firebase_admin.initialize_app(cred)
        except ValueError as e:
            print(e)
            print("Firebase Admin SDK not found")
