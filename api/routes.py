# api/routes.py

from fastapi import APIRouter, Depends
from api.auth import verify
from core.dependencies import get_predictor
from core.inference import DiabetesPredictor
from validation import PatientData

router = APIRouter()


# Корневой эндпоинт
@router.get("/", summary="Приветственное сообщение", tags=["Предсказание диабета"])
def root():
    return {"message": "ML Diabetes Prediction API"}

@router.post("/predict", summary="Отправка данных на проверку",
             tags=["Проверка показателей на диабет"])
def predict(
        data: PatientData,
        username: str = Depends(verify),
        predictor: DiabetesPredictor = Depends(get_predictor),
):
    prediction = predictor.predict(
        data.Pregnancies,
        data.Glucose,
        data.BMI,
        data.Age
    )

    return {"prediction": prediction}
