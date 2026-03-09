# core/password_service.py
import bcrypt

class PasswordService:
    """
    Сервис для работы с паролями пользователей.

    Отвечает за:
    - хэширование паролей
    - проверку пароля при аутентификации

    Использует библиотеку bcrypt.
    """

    @classmethod
    def hash_password(
            cls,
            password: str) -> str:
        """
        Хэширует пароль пользователя.
        :param password: исходный пароль пользователя.
        :return: безопасный bcrypt-хэш пароля.
        """
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    @classmethod
    def verify_password(
            cls,
            password: str,
            password_hash: str) -> bool:
        """
        Проверяет соответствие пароля его хэшу.
        :param password: пароль, введённый пользователем.
        :param password_hash: сохранённый в базе хэш пароля.
        :return: True если пароль корректный, иначе False.
        """
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )
