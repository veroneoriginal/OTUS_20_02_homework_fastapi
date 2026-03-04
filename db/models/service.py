# db/models/service.py
from sqlalchemy.orm import Session
from db.models.user import User


def get_user_by_email(email: str, db: Session):
    """
    Функция для проверки наличия пользователя в базе
    """
    return db.query(User).filter(User.email == email).first()
