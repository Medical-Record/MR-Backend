from fastapi import APIRouter, Depends, HTTPException
from contexts.patient_management.application.use_cases.create_patient_use_case import CreatePatientUseCase
from contexts.patient_management.application.use_cases.update_patient_use_case import UpdatePatientUseCase
from contexts.patient_management.application.use_cases.delete_patient_use_case import DeletePatientUseCase
from contexts.patient_management.application.use_cases.get_patient_use_case import GetPatientUseCase
from contexts.patient_management.infrastructure.repositories.patient_repository import PatientRepository
from contexts.patient_management.application.dtos.patient_request import PatientRequest
from contexts.patient_management.application.dtos.patient_update_request import PatientUpdateRequest
from contexts.patient_management.application.dtos.patient_response import PatientResponse

# Asegurar que el prefix y tags están definidos
router = APIRouter(prefix="/patients", tags=["Patient Management"])

# Funciones para inyección de dependencias
def get_patient_repository():
    return PatientRepository()

def get_create_patient_use_case(patient_repository: PatientRepository = Depends(get_patient_repository)):
    return CreatePatientUseCase(patient_repository)

def get_update_patient_use_case(patient_repository: PatientRepository = Depends(get_patient_repository)):
    return UpdatePatientUseCase(patient_repository)

def get_delete_patient_use_case(patient_repository: PatientRepository = Depends(get_patient_repository)):
    return DeletePatientUseCase(patient_repository)

def get_get_patient_use_case(patient_repository: PatientRepository = Depends(get_patient_repository)):
    return GetPatientUseCase(patient_repository)

@router.post("/", response_model=PatientResponse)
def create_patient(
    patient_request: PatientRequest,
    create_patient_use_case: CreatePatientUseCase = Depends(get_create_patient_use_case)
):
    return create_patient_use_case.execute(patient_request)

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: str,
    get_patient_use_case: GetPatientUseCase = Depends(get_get_patient_use_case)
):
    return get_patient_use_case.execute(patient_id)

@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: str,
    patient_update_request: PatientUpdateRequest,
    update_patient_use_case: UpdatePatientUseCase = Depends(get_update_patient_use_case)
):
    updated_patient = update_patient_use_case.execute(patient_id, patient_update_request)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

@router.delete("/{patient_id}")
def delete_patient(
    patient_id: str,
    delete_patient_use_case: DeletePatientUseCase = Depends(get_delete_patient_use_case)
):
    delete_patient_use_case.execute(patient_id)
    return {"message": "Patient deleted successfully"}
