import pymongo

from ..core.config import settings


def get_db(client: pymongo.MongoClient) -> pymongo.database.Database:
    return client[settings.DATABASE_NAME]


def get_db_collection(client: pymongo.MongoClient, name: str) -> pymongo.collection.Collection:
    return get_db(client)[name]
