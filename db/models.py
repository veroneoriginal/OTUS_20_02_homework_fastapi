# db/models.py
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    """
    ORM-модель для хранения истории предсказаний диабета.
    Содержит входные параметры запроса и результат инференса модели.
    """
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    pregnancies = Column(Integer)
    glucose = Column(Float)
    bmi = Column(Float)
    age = Column(Integer)

    result = Column(Integer)
