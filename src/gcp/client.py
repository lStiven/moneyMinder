from injector import singleton
from firebase_admin import firestore


@singleton
class DBInjector:
    def __init__(self):
        self.client = firestore.client()
