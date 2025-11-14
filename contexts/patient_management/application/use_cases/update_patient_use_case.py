from contexts.patient_management.infrastructure.repositories.patient_repository import PatientRepository
from contexts.patient_management.application.dtos.patient_update_request import PatientUpdateRequest

class UpdatePatientUseCase:
    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository

    def execute(self, patient_id: str, patient_update_request: PatientUpdateRequest):
        patient = self.patient_repository.find_by_id(patient_id)
        if patient:
            patient.update(**patient_update_request.dict())
            self.patient_repository.update(patient)
            return patient
        return None
