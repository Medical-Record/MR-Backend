from pydantic import BaseModel

class AuthResponse(BaseModel):
    user_id: str
    email: str
    token: str
