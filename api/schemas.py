# api/schemas.py
# Валидация входных данных через pydantic-модель
from pydantic import BaseModel

class PatientRequest(BaseModel):
    Pregnancies: int
    Glucose: float
    BMI: float
    Age: int
