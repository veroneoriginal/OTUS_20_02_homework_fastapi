# core/inference.py
import numpy as np
from onnxruntime import InferenceSession


class DiabetesPredictor:
    """
    Сервис для выполнения инференса модели диабета.
    """

    def __init__(self, session: InferenceSession):
        self.session = session
        self.input_name = session.get_inputs()[0].name

    def predict(self, pregnancies, glucose, bmi, age) -> int:
        """
        Подготовка входа для ONNX
        :param pregnancies:
        :param glucose:
        :param bmi:
        :param age:
        :return: результат прогноза
        """
        input_data = np.array([[
            pregnancies,
            glucose,
            bmi,
            age
        ]], dtype=np.float32)

        # Модель возвращает два выхода: [array([1], dtype=int64), [{0: 0.0, 1: 1.0}]]
        output = self.session.run(
            None,
            {self.input_name: input_data},
        )

        probability = float(output[0].squeeze())

        return 1 if probability > 0.5 else 0
