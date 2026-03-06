# api/jwt_auth.py

import logging
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from config import settings

logger = logging.getLogger(__name__)

# Позволяет верифицировать запросы на основе токена
security = HTTPBearer()


def get_current_user(
        # Authorization: Bearer <token>
        credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    Извлекает и проверяет JWT access-token из Authorization: Bearer.

    Возвращает payload токена (например: sub, role).
    При невалидном токене выбрасывает HTTP 401.
    """

    token = credentials.credentials

    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )

    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        ) from exc


def require_role(required_roles: list[str]):
    """
    Фабрика для проверки роли пользователя (RBAC).

    1. извлекает пользователя из JWT
    2. проверяет его роль
    """

    def role_checker(user=Depends(get_current_user)):

        user_role = user.get("role")

        if user_role not in required_roles:

            logger.warning(
                f"Access denied for user {user.get('sub')} with role {user_role}"
            )

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )

        return user

    return role_checker
