# db/models/user.py
from sqlalchemy import Column, Integer, String
from db.models.base import Base

class User(Base):
    """
    ORM-модель пользователя.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="user")
