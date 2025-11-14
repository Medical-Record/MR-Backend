from pydantic import BaseModel
from datetime import date

class DoctorResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    specialty: str
    license_number: str
    hire_date: date
