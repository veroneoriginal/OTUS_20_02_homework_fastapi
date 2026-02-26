# main.py

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="ML Diabetes Prediction API")

app.include_router(router)
