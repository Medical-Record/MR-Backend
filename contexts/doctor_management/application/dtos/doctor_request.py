from pydantic import BaseModel
from datetime import date

class DoctorRequest(BaseModel):
    first_name: str
    last_name: str
    specialty: str
    license_number: str
    hire_date: date
