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
    JWT_REFRESH_EXPIRE_DAYS: int

    # ===== DATABASE =====
    DATABASE_URL: str

    # ===== ADMIN SEED =====
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    # ===== SECURITY =====
    MAX_LOGIN_ATTEMPTS: int = 5
    LOCKOUT_MINUTES: int = 15

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",

    )


settings = Settings()
