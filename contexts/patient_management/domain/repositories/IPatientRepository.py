from abc import ABC, abstractmethod
from contexts.patient_management.domain.entities.patient import Patient

class IPatientRepository(ABC):
    @abstractmethod
    def add(self, patient: Patient):
        pass

    @abstractmethod
    def update(self, patient: Patient):
        pass

    @abstractmethod
    def delete(self, patient_id: str):
        pass

    @abstractmethod
    def find_by_id(self, patient_id: str) -> Patient:
        pass
