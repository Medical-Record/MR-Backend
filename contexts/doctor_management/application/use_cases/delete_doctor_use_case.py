from contexts.doctor_management.domain.repositories.IDoctorRepository import IDoctorRepository

class DeleteDoctorUseCase:
    def __init__(self, doctor_repository: IDoctorRepository):
        self.doctor_repository = doctor_repository

    def execute(self, doctor_id: str) -> bool:
        doctor = self.doctor_repository.find_by_id(doctor_id)
        if not doctor:
            return False  # No encontrado
        self.doctor_repository.delete(doctor_id)
        return True  # Eliminado con éxito
