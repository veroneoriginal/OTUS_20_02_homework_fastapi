# core/dependencies.py
from fastapi import Depends

from core.inference import DiabetesPredictor
from core.model_loader import load_session
from services.prediction_service import PredictionService

# создаётся один раз при старте приложения
session = load_session()
predictor = DiabetesPredictor(session=session)


def get_predictor() -> DiabetesPredictor:
    return predictor


def get_prediction_service(
        func_predictor: DiabetesPredictor = Depends(get_predictor),
) -> PredictionService:
    return PredictionService(predictor=func_predictor)
