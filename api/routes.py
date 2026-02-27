# api/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.auth import verify
from api.schemas import PatientRequest
from core.dependencies import get_predictor
from core.inference import DiabetesPredictor
from db.dependencies import get_db
from services.prediction_service import PredictionService

# Содержит зарегистрированные эндпоинты
# APIRouter - это способ разделить маршруты по модулям
router = APIRouter()


# Корневой эндпоинт
@router.get("/", summary="Приветственное сообщение", tags=["Предсказание диабета"])
def root():
    return {"message": "ML Diabetes Prediction API"}


@router.post("/predict", summary="Отправка данных на проверку",
             tags=["Проверка показателей на диабет"])
def predict(
        data: PatientRequest,
        # pylint: disable=W0613 (unused-argument)
        username: str = Depends(verify),
        predictor: DiabetesPredictor = Depends(get_predictor),
        db: Session = Depends(get_db),
):
    service = PredictionService(predictor=predictor)

    prediction = service.predict_and_save(db=db, data=data)

    return {
        "id": prediction.id,
        "prediction": prediction.result
    }
