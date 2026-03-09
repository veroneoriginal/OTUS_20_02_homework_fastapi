# db/models/refresh_token.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from db.models.base import Base


class RefreshToken(Base):
    """
    ORM-модель для хранения refresh-токенов.
    Хранит хэш токена, а не сам токен.
    """
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token_hash = Column(String, nullable=False, index=True)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked = Column(Boolean, default=False)
