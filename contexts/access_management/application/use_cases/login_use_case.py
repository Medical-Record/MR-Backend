from contexts.access_management.domain.services.auth_service import AuthService
from contexts.access_management.domain.repositories.IUserRepository import IUserRepository

class LoginUseCase:
    """Caso de uso para iniciar sesión."""

    def __init__(self, user_repository: IUserRepository):
        self.auth_service = AuthService(user_repository)

    def execute(self, email: str, password: str) -> bool:
        """Ejecuta la autenticación de usuario."""
        return self.auth_service.authenticate_user(email, password)
