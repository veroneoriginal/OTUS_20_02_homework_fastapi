# api/schemas.py
# Валидация входных данных через pydantic-модель
from pydantic import BaseModel, Field


class PatientRequest(BaseModel):
    """
    Запрос от пациента/пользователя
    """

    # ge — больше или равно / le — меньше или равно
    Pregnancies: int = Field(ge=0, le=20)
    Glucose: float = Field(ge=0, le=300)
    BMI: float = Field(ge=10, le=80)
    Age: int = Field(ge=0, le=120)


class UserCreate(BaseModel):
    """
    Схема запроса для регистрации пользователя.
    """
    email: str
    password: str


class LoginRequest(BaseModel):
    """
    Схема запроса для аутентификации пользователя.
    """
    email: str
    password: str
