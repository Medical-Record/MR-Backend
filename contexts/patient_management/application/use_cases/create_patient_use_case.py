from contexts.patient_management.domain.entities.patient import Patient
from contexts.patient_management.infrastructure.repositories.patient_repository import PatientRepository
from contexts.patient_management.application.dtos.patient_request import PatientRequest
from fastapi import Depends

class CreatePatientUseCase:
    def __init__(self, patient_repository: PatientRepository = Depends()):
        self.patient_repository = patient_repository

    def execute(self, patient_request: PatientRequest):
        patient = Patient(**patient_request.dict())
        self.patient_repository.add(patient)
        return patient