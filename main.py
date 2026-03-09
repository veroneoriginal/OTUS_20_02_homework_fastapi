# main.py

from fastapi import FastAPI
from api.routes import router
from db.models.base import Base
from db.session import engine, SessionLocal
from db.models.user import User
# pylint: disable=unused-import
from db.models.refresh_token import RefreshToken
from db.models.service import get_user_by_email
from core.password_service import PasswordService
from config import settings

# Создаётся главный объект приложения
app = FastAPI(title="ML Diabetes Prediction API")

# Добавляю все маршруты, которые лежат внутри routers, в основное приложение
app.include_router(router)

def seed_admin():
    """
    Создаёт администратора при первом запуске приложения.

    Проверяет наличие пользователя с email из настроек (ADMIN_EMAIL).
    Если такого пользователя нет — создаёт его с ролью 'admin'.
    Повторный запуск безопасен: дубликат не создаётся.
    """
    db = SessionLocal()
    try:
        existing = get_user_by_email(email=settings.ADMIN_EMAIL, db=db)
        if not existing:
            admin = User(
                email=settings.ADMIN_EMAIL,
                password_hash=PasswordService.hash_password(settings.ADMIN_PASSWORD),
                role="admin",
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

seed_admin()
