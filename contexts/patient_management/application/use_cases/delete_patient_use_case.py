from contexts.patient_management.infrastructure.repositories.patient_repository import PatientRepository
from fastapi import Depends

class DeletePatientUseCase:
    def __init__(self, patient_repository: PatientRepository = Depends()):
        self.patient_repository = patient_repository

    def execute(self, patient_id: str):
        self.patient_repository.delete(patient_id)
