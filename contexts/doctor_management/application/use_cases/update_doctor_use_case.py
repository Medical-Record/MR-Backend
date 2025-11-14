from contexts.doctor_management.domain.repositories.IDoctorRepository import IDoctorRepository
from contexts.doctor_management.application.dtos.doctor_update_request import DoctorUpdateRequest

class UpdateDoctorUseCase:
    def __init__(self, doctor_repository: IDoctorRepository):
        self.doctor_repository = doctor_repository

    def execute(self, doctor_id: str, request: DoctorUpdateRequest) -> bool:
        doctor = self.doctor_repository.find_by_id(doctor_id)
        if not doctor:
            return False  # No encontrado

        doctor.update(
            first_name=request.first_name,
            last_name=request.last_name,
            specialty=request.specialty,
            license_number=request.license_number
        )

        self.doctor_repository.update(doctor)
        return True  # Actualizado con éxito
