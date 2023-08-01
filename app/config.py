from typing import Any, Callable, Set

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'hask777'
    DB_PASS: str = 'lara'
    DB_NAME: str = 'shumeiko'

    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')

print(settings.DB_HOST)



