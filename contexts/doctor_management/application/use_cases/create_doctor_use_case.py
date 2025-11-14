from contexts.doctor_management.domain.repositories.IDoctorRepository import IDoctorRepository
from contexts.doctor_management.domain.entities.doctor import Doctor
from contexts.doctor_management.application.dtos.doctor_request import DoctorRequest

class CreateDoctorUseCase:
    def __init__(self, doctor_repository: IDoctorRepository):
        self.doctor_repository = doctor_repository

    def execute(self, request: DoctorRequest) -> Doctor:
        doctor = Doctor(**request.dict())
        return self.doctor_repository.create(doctor)
