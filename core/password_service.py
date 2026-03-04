# core/password_service.py

from passlib.context import CryptContext


class PasswordService:
    """
    Сервис для работы с паролями пользователей.

    Отвечает за:
    - хэширование паролей
    - проверку пароля при аутентификации

    Использует алгоритм bcrypt через библиотеку passlib.
    """

    _pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
    )

    @classmethod
    def hash_password(
            cls,
            password: str) -> str:
        """
        Хэширует пароль пользователя.
        :param password: исходный пароль пользователя.
        :return: безопасный bcrypt-хэш пароля.
        """
        return cls._pwd_context.hash(password)

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
        return cls._pwd_context.verify(password, password_hash)
