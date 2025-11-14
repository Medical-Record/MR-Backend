from contexts.doctor_management.domain.repositories.IDoctorRepository import  IDoctorRepository
from contexts.doctor_management.domain.entities.doctor import Doctor
from typing import Optional, List

class DoctorRepository(IDoctorRepository):
    def __init__(self):
        self.doctors = {}

    def create(self, doctor: Doctor) -> Doctor:
        self.doctors[doctor.id] = doctor
        return doctor

    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        return self.doctors.get(doctor_id)

    def update(self, doctor: Doctor) -> None:
        if doctor.id in self.doctors:
            self.doctors[doctor.id] = doctor

    def delete(self, doctor_id: str) -> None:
        self.doctors.pop(doctor_id, None)
