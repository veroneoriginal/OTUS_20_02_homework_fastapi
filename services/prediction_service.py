# services/prediction_service.py
from sqlalchemy.orm import Session
from db.models import Prediction
from core.inference import DiabetesPredictor
from api.schemas import PatientRequest

class PredictionService:
    """
    Сервисный слой для координации инференса модели
    и сохранения результата в базе данных.
    """

    def __init__(self, predictor: DiabetesPredictor):
        """
        Инициализирует сервис с ML-предиктором.
        """
        self.predictor = predictor

    def predict_and_save(self, db: Session, data: PatientRequest):
        """
        Выполняет предсказание и сохраняет результат в БД.
        """
        result = self.predictor.predict(
            data.Pregnancies,
            data.Glucose,
            data.BMI,
            data.Age
        )

        db_obj = Prediction(
            pregnancies=data.Pregnancies,
            glucose=data.Glucose,
            bmi=data.BMI,
            age=data.Age,
            result=result,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj
