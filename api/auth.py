# api/auth.py
# Базовая авторизация по логину и паролю через HTTP-заголовок.

import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config import settings

# Сервер НЕ хранит состояние авторизации.
security = HTTPBasic()



def verify(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    """
    Проверяет HTTP Basic учетные данные
    и возвращает имя пользователя при успехе.
    В случае ошибки — выбрасывает 401.
    """
    correct_username = secrets.compare_digest(
        credentials.username,
        settings.API_USERNAME,
    )

    correct_password = secrets.compare_digest(
        credentials.password,
        settings.API_PASSWORD,
    )

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Basic"},
        )

    # Это логин, который пользователь ввёл в Basic Auth
    return credentials.username
