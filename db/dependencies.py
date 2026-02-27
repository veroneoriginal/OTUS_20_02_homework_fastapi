# db/dependencies.py
from db.session import SessionLocal

def get_db():
    """
    Предоставляет SQLAlchemy-сессию на время одного запроса
    и автоматически закрывает её после выполнения.
    :return: сессию
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
