import bcrypt
from contexts.access_management.domain.repositories.IUserRepository import IUserRepository
from contexts.access_management.domain.entities.user import User

class AuthService:
    """Servicio de autenticación que usa un repositorio de usuarios."""

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def register_user(self, name: str, email: str, password: str, user_type: str):
        """Registra un usuario encriptando su contraseña."""
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(name=name, email=email, password=hashed_password, user_type=user_type)
        self.user_repository.save(user)
        return user

    def authenticate_user(self, email: str, password: str) -> bool:
        """Autentica un usuario verificando su contraseña."""
        user = self.user_repository.find_by_email(email)
        if not user:
            return False
        return bcrypt.checkpw(password.encode(), user.password.encode())
