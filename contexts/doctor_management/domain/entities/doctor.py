from datetime import date
from typing import Optional
import uuid

class Doctor:
    def __init__(self,
                 id: Optional[str] = None,
                 first_name: str = "",
                 last_name: str = "",
                 specialty: str = "",
                 license_number: str = "",
                 hire_date: Optional[date] = None):
        self.id = id or str(uuid.uuid4())  # Generación de UUID si no se proporciona
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.license_number = license_number
        self.hire_date = hire_date or date.today()

    def update(self, first_name: str, last_name: str, specialty: str, license_number: str):
        """ Método para actualizar los datos de un doctor """
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
        self.license_number = license_number
