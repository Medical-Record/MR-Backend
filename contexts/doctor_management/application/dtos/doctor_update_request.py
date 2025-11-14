from pydantic import BaseModel

class DoctorUpdateRequest(BaseModel):
    first_name: str
    last_name: str
    specialty: str
    license_number: str
