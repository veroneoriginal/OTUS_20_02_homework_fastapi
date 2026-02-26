import logging
import numpy
from fastapi import FastAPI, Depends, HTTPException
from authentication import verify
from inference import session
from validation import PatientData


logging.basicConfig(level=logging.INFO)

app = FastAPI()


# Корневой эндпоинт
@app.get("/", summary="Приветственное сообщение", tags=["Предсказание диабета"])
def root():
    return {"message": "ML Diabetes Prediction API"}


# Эндпоинт, доступный только авторизованным пользователям
@app.post("/predict", summary="Отправка данных на проверку",
          tags=["Проверка показателей на диабет"])
def predict(data: PatientData, username: str = Depends(verify)):

    logging.info("User %s made prediction request", username)

    # Подготовка входа для ONNX
    input_data = numpy.array([[
        data.Pregnancies,
        data.Glucose,
        data.BMI,
        data.Age
    ]], dtype=numpy.float32)

    # Получаем имя входного слоя модели
    # объект InferenceSession — обёртка над ONNX-моделью.
    input_name = session.get_inputs()[0].name

    # Инференс
    try:
        # Модель возвращает два выхода: [array([1], dtype=int64), [{0: 0.0, 1: 1.0}]]
        output = session.run(None, {input_name: input_data})
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Model inference error") from e

    probability = float(output[0].squeeze()) # 1.0

    # Вывод результата
    prediction = 1 if probability > 0.5 else 0

    return {"prediction": prediction}
