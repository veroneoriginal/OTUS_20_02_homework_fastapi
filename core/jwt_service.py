# core/jwt_service.py

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

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_EXPIRE_MINUTES
        )

        now = datetime.now(timezone.utc)

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
    def decode_token(cls, token: str) -> dict:

        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
