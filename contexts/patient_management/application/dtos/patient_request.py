from pydantic import BaseModel

class PatientRequest(BaseModel):
    name: str
    age: int
    gender: str
    diagnosis: str
