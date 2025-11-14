from pydantic import BaseModel

class PatientUpdateRequest(BaseModel):
    name: str
    age: int
    diagnosis: str
