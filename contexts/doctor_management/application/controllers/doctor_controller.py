from fastapi import APIRouter, Depends, HTTPException
from contexts.doctor_management.application.dtos.doctor_request import DoctorRequest
from contexts.doctor_management.application.dtos.doctor_response import DoctorResponse
from contexts.doctor_management.application.dtos.doctor_update_request import DoctorUpdateRequest
from contexts.doctor_management.application.use_cases.create_doctor_use_case import CreateDoctorUseCase
from contexts.doctor_management.application.use_cases.get_doctor_use_case import GetDoctorUseCase
from contexts.doctor_management.application.use_cases.update_doctor_use_case import UpdateDoctorUseCase
from contexts.doctor_management.application.use_cases.delete_doctor_use_case import DeleteDoctorUseCase
from contexts.doctor_management.infrastructure.repositories.doctor_repository import DoctorRepository

router = APIRouter(prefix="/doctors", tags=["Doctor Management"])
doctor_repository = DoctorRepository()

@router.post("/", response_model=DoctorResponse, status_code=201)
def create_doctor(request: DoctorRequest):
    """ Crear un nuevo doctor """
    use_case = CreateDoctorUseCase(doctor_repository)
    doctor = use_case.execute(request)
    return DoctorResponse(**doctor.__dict__)

@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: str):
    """ Obtener un doctor por ID """
    use_case = GetDoctorUseCase(doctor_repository)
    doctor = use_case.execute(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.put("/{doctor_id}", status_code=204)
def update_doctor(doctor_id: str, request: DoctorUpdateRequest):
    """ Actualizar datos de un doctor """
    use_case = UpdateDoctorUseCase(doctor_repository)
    success = use_case.execute(doctor_id, request)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return

@router.delete("/{doctor_id}", status_code=204)
def delete_doctor(doctor_id: str):
    """ Eliminar un doctor """
    use_case = DeleteDoctorUseCase(doctor_repository)
    success = use_case.execute(doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return
