import pymongo
from ..core.config import settings

client = pymongo.MongoClient(settings.DATABASE_URL)
