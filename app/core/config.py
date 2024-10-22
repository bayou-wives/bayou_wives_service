import os
import urllib.parse

from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    ENV: str = os.getenv('ENV', 'local')
    # DB configs
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'db_user')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', '')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'db')
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def compile_db_connection(cls, v: Optional[str], values: ValidationInfo) -> PostgresDsn:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get('POSTGRES_USER'),
            password=urllib.parse.quote(values.data.get('POSTGRES_PASSWORD')),
            host=values.data.get('POSTGRES_SERVER'),
            port=values.data.get('POSTGRES_PORT'),
            path=values.data.get('POSTGRES_DB')
        )


settings = Settings()
