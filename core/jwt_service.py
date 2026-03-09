# core/jwt_service.py

import secrets
from datetime import datetime, timedelta, timezone
from jose import jwt
from config import settings


class JWTService:
    """
    Сервис для работы с JWT-токенами.

    Отвечает за создание и проверку JWT access-токенов,
    используемых для аутентификации пользователей.
    """

    @classmethod
    def create_access_token(
            cls,
            data: dict) -> str:
        """
        Создаёт JWT access-токен.

        :param data: данные payload (например user_id и роль).
        :return: закодированный JWT токен.
        """

        to_encode = data.copy()

        now = datetime.now(timezone.utc)

        expire = now + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)

        to_encode.update(
            {
                "exp": expire,
                "iat": now,
            }
        )

        encoded_jwt = jwt.encode(
            to_encode,
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )

        return encoded_jwt

    @classmethod
    def create_refresh_token(cls) -> tuple[str, datetime]:
        """
        Создаёт refresh-токен.
        Возвращает сам токен и время его истечения.
        Токен — случайная строка, не JWT.
        """
        token = secrets.token_urlsafe(32)
        expires_at = datetime.now(timezone.utc) + timedelta(
            days=settings.JWT_REFRESH_EXPIRE_DAYS
        )
        return token, expires_at
