# validation.py
# Валидация входных данных через pydantic-модель
from pydantic import BaseModel

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BMI: float
    Age: int
