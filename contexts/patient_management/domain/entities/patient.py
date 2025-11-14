from pydantic import BaseModel
from uuid import uuid4

class Patient(BaseModel):
    id: str = None
    name: str
    age: int
    gender: str
    diagnosis: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.id:
            self.id = str(uuid4())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
