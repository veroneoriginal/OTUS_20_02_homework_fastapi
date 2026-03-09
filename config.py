# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Конфигурация приложения.
    Значения берутся из .env файла.
    """
    # ===== ML =====
    MODEL_PATH: str

    # ===== AUTH =====
    API_USERNAME: str
    API_PASSWORD: str

    # ===== JWT =====
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    # ===== DATABASE =====
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",

    )


settings = Settings()
