# core/dependencies.py
from core.inference import DiabetesPredictor
from core.model_loader import load_session

# создаётся один раз при старте приложения
session = load_session()
predictor = DiabetesPredictor(session=session)


def get_predictor() -> DiabetesPredictor:
    return predictor
