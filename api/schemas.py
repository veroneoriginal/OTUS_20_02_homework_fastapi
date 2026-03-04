# api/schemas.py
# Валидация входных данных через pydantic-модель
from pydantic import BaseModel

class PatientRequest(BaseModel):
    """
    Запрос от пациента/пользователя
    """
    Pregnancies: int
    Glucose: float
    BMI: float
    Age: int


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
