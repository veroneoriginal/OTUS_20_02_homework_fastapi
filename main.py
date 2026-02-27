# main.py

from fastapi import FastAPI
from api.routes import router
from db.models import Base
from db.session import engine

Base.metadata.create_all(bind=engine)

# Создаётся главный объект приложения
app = FastAPI(title="ML Diabetes Prediction API")

# Добавляю все маршруты, которые лежат внутри routers, в основное приложение
app.include_router(router)
