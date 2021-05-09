import pymongo

from ..core.config import settings
from ..models.user import UserInDB
from .deps import get_db_collection


def init_db(client: pymongo.MongoClient) -> None:
    # update admin user in db
    collection = get_db_collection(client, settings.DATABASE_USER_COLLECTION)
    user = UserInDB(**{
        "username": settings.ADMIN_USERNAME,
        "hashed_password": settings.ADMIN_HASHED_PASSWORD
    })
    user_dict = collection.find_one({ "username": user.username })
    if user_dict:
        r = collection.replace_one({ "username": user.username }, user.dict())
    else:
        collection.insert_one(user.dict())


def close_db(client: pymongo.MongoClient) -> None:
    client.close()
