from contexts.access_management.domain.repositories.IUserRepository import IUserRepository
from contexts.access_management.domain.entities.user import User
from contexts.access_management.infrastructure.adapters.firebase_auth_adapter import db

class UserRepository(IUserRepository):
    """Implementación de IUserRepository para interactuar con Firestore."""

    def __init__(self):
        self.collection = db.collection("usuarios")

    def save(self, user: User):
        """Guarda un usuario en Firestore."""
        user_ref = self.collection.document(user.id)
        user_ref.set(user.to_dict())

    def find_by_email(self, email: str) -> User:
        """Busca un usuario por email en Firestore y devuelve un objeto User."""
        query = self.collection.where("email", "==", email).limit(1).stream()
        for doc in query:
            user_data = doc.to_dict()
            return User(**user_data)
        return None
