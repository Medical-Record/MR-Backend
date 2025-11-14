from contexts.access_management.domain.services.auth_service import AuthService
from contexts.access_management.domain.repositories.IUserRepository import IUserRepository

class RegisterUserUseCase:
    """Caso de uso para registrar un usuario."""

    def __init__(self, user_repository: IUserRepository):
        self.auth_service = AuthService(user_repository)

    def execute(self, name: str, email: str, password: str, user_type: str):
        """Ejecuta el registro de usuario."""
        return self.auth_service.register_user(name, email, password, user_type)
