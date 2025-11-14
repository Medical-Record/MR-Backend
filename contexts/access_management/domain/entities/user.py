class User:
    def __init__(self, id: str, email: str, password: str, token: str = None):
        self.id = id
        self.email = email
        self.password = password  # Encriptada
        self.token = token
