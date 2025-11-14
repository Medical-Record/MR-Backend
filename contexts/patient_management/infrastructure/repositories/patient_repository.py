from contexts.patient_management.domain.repositories.IPatientRepository import IPatientRepository
from contexts.patient_management.domain.entities.patient import Patient
from typing import Dict
from fastapi import HTTPException

class PatientRepository(IPatientRepository):
    def __init__(self):
        self.patients: Dict[str, Patient] = {}  # Simulación de base de datos en memoria

    def add(self, patient: Patient):
        self.patients[patient.id] = patient

    def update(self, patient: Patient):
        if patient.id in self.patients:
            self.patients[patient.id] = patient
        else:
            raise HTTPException(status_code=404, detail="Patient not found")

    def delete(self, patient_id: str):
        if patient_id in self.patients:
            del self.patients[patient_id]
        else:
            raise HTTPException(status_code=404, detail="Patient not found")

    def find_by_id(self, patient_id: str) -> Patient:
        if patient_id in self.patients:
            return self.patients[patient_id]
        raise HTTPException(status_code=404, detail="Patient not found")
