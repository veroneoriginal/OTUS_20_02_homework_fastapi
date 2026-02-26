# Загрузка модели машинного обучения
import os
import onnxruntime
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

session = onnxruntime.InferenceSession(
    MODEL_PATH,
    providers=["CPUExecutionProvider"]
)
