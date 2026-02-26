# core/model_loader.py

import onnxruntime
from config import settings


def load_session() -> onnxruntime.InferenceSession:
    """
    Загружает ONNX модель и возвращает сессию инференса.
    """
    return onnxruntime.InferenceSession(
        settings.MODEL_PATH,
        providers=["CPUExecutionProvider"]
    )
