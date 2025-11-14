from contexts.doctor_management.domain.repositories.IDoctorRepository import IDoctorRepository
from contexts.doctor_management.application.dtos.doctor_response import DoctorResponse
from typing import Optional

class GetDoctorUseCase:
    def __init__(self, doctor_repository: IDoctorRepository):
        self.doctor_repository = doctor_repository

    def execute(self, doctor_id: str) -> Optional[DoctorResponse]:
        doctor = self.doctor_repository.find_by_id(doctor_id)
        if not doctor:
            return None
        return DoctorResponse(**doctor.__dict__)
