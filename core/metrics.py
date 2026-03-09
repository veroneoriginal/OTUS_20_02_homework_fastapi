# core/metrics.py
from datetime import datetime, timezone


class Metrics:
    """
    Простое хранилище метрик приложения.
    Данные хранятся в памяти — сбрасываются при перезапуске.
    """

    _inference_count: int = 0
    _start_time: datetime = datetime.now(timezone.utc)

    @classmethod
    def increment_inference(cls) -> None:
        """
        Увеличивает счётчик инференсов на 1.
        """
        cls._inference_count += 1

    @classmethod
    def get_inference_count(cls) -> int:
        """
        Возвращает количество выполненных инференсов.
        """
        return cls._inference_count

    @classmethod
    def get_uptime_seconds(cls) -> int:
        """
        Возвращает время работы приложения в секундах.
        """
        delta = datetime.now(timezone.utc) - cls._start_time
        return int(delta.total_seconds())
