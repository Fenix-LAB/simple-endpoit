import os
import json

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080


class ProductionConfig(Config):
    DEBUG: bool = False
    APP_HOST: str = "192.168.1.100"
    APP_PORT: int = 9000
    JWT_SECRET: str = "s3cr3tK3yR4nd0m"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    EXCLUDED_URLS: list[str] = ["/health", "/docs", "/openapi.json"]
    ROUTE_PATH: str = "/api/prod"


class TestConfig(ProductionConfig):
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"


class LocalConfig(Config):
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    ROUTE_PATH: str = "/api/v1"

def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
