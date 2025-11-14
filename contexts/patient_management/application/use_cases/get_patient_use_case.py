from contexts.patient_management.infrastructure.repositories.patient_repository import PatientRepository
from contexts.patient_management.application.dtos.patient_response import PatientResponse
from fastapi import Depends

class GetPatientUseCase:
    def __init__(self, patient_repository: PatientRepository = Depends()):
        self.patient_repository = patient_repository

    def execute(self, patient_id: str):
        patient = self.patient_repository.find_by_id(patient_id)
        if patient:
            return PatientResponse.from_orm(patient)
        return None
