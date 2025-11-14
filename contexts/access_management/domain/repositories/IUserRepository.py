from abc import ABC, abstractmethod
from contexts.access_management.domain.entities.user import User

class IUserRepository(ABC):
    """Interfaz para UserRepository, que define los métodos obligatorios."""

    @abstractmethod
    def save(self, user: User):
        """Guarda un usuario en la base de datos."""
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """Busca un usuario por email y devuelve una instancia de User si existe."""
        pass
