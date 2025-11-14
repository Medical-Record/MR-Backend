from abc import ABC, abstractmethod
from contexts.doctor_management.domain.entities.doctor import Doctor
from typing import Optional, List

class IDoctorRepository(ABC):
    @abstractmethod
    def create(self, doctor: Doctor) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        pass

    @abstractmethod
    def update(self, doctor: Doctor) -> None:
        pass

    @abstractmethod
    def delete(self, doctor_id: str) -> None:
        pass
