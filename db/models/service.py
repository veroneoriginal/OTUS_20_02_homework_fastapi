# db/models/service.py
import hashlib
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from db.models.user import User
from db.models.refresh_token import RefreshToken
from config import settings


def get_user_by_email(
        email: str,
        db: Session,
) -> User | None:
    """
    Функция для проверки наличия пользователя в базе
    """
    return db.query(User).filter(User.email == email).first()


def hash_token(token: str) -> str:
    """
    Хэширует refresh-токен через SHA-256.
    """
    return hashlib.sha256(token.encode()).hexdigest()


def save_refresh_token(
        user_id: int,
        token: str,
        expires_at: datetime,
        db: Session,
):
    """
    Сохраняет хэш refresh-токена в БД.
    """
    db_token = RefreshToken(
        user_id=user_id,
        token_hash=hash_token(token),
        expires_at=expires_at,
    )
    db.add(db_token)
    db.commit()


def get_refresh_token(
        token: str,
        db: Session,
) -> RefreshToken | None:
    """
    Ищет refresh-токен в БД по хэшу.
    """
    return db.query(RefreshToken).filter(
        RefreshToken.token_hash == hash_token(token),
        # pylint: disable=singleton-comparison
        RefreshToken.revoked == False,
        RefreshToken.expires_at > datetime.now(timezone.utc),
    ).first()


def revoke_refresh_token(
        token: str,
        db: Session,
):
    """
    Отзывает refresh-токен (logout).
    """
    db_token = get_refresh_token(token=token, db=db)
    if db_token:
        db_token.revoked = True
        db.commit()


def is_account_locked(user: User) -> bool:
    """
    Проверяет, заморожен ли аккаунт.
    Возвращает True если заморозка ещё активна.
    """
    if user.locked_until is None:
        return False

    # SQLite возвращает datetime без timezone, приводим к UTC
    locked_until = user.locked_until.replace(tzinfo=timezone.utc)
    return locked_until > datetime.now(timezone.utc)


def record_failed_login(user: User, db: Session) -> None:
    """
    Увеличивает счётчик неудачных попыток.
    При достижении лимита — замораживает аккаунт.
    """
    user.failed_login_attempts += 1

    if user.failed_login_attempts >= settings.MAX_LOGIN_ATTEMPTS:
        user.locked_until = datetime.now(timezone.utc) + timedelta(
            minutes=settings.LOCKOUT_MINUTES
        )

    db.commit()


def reset_failed_logins(
        user: User,
        db: Session,
) -> None:
    """
    Сбрасывает счётчик неудачных попыток после успешного входа.
    """
    user.failed_login_attempts = 0
    user.locked_until = None
    db.commit()
