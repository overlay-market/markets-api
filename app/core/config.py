import os
import secrets

from pathlib import Path
from pydantic import BaseSettings


DEFAULT_ABI = os.path.join(Path(__file__).resolve().parents[1], 'abi/')

class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    BROWNIE_NETWORK: str = 'development'
    ABI_DIR: str = DEFAULT_ABI

    DATABASE_URL: str = 'mongodb://localhost:27017'
    DATABASE_NAME: str = 'farms'

    DATABASE_USER_COLLECTION: str = 'user'

    ADMIN_USERNAME: str
    ADMIN_HASHED_PASSWORD: str

    class Config:
        case_sensitive = True


settings = Settings()
