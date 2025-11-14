from pydantic import BaseModel

class PatientResponse(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    diagnosis: str

    class Config:
        from_attributes = True
