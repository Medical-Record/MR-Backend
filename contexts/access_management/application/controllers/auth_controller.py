from fastapi import APIRouter, Depends, HTTPException
from contexts.access_management.application.dtos.auth_request import AuthRequest
from contexts.access_management.application.dtos.auth_response import AuthResponse
from contexts.access_management.application.use_cases.login_use_case import LoginUseCase
from contexts.access_management.application.use_cases.register_user_use_case import RegisterUserUseCase
from contexts.access_management.infrastructure.repositories.user_repository import UserRepository
from contexts.access_management.domain.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

# 🔹 Funciones para inyección de dependencias
def get_register_use_case():
    user_repository = UserRepository()
    auth_service = AuthService(user_repository)
    return RegisterUserUseCase(auth_service)

def get_login_use_case():
    user_repository = UserRepository()
    auth_service = AuthService(user_repository)
    return LoginUseCase(auth_service)

@router.post("/register", response_model=AuthResponse)
def register(
    auth_request: AuthRequest,
    register_use_case: RegisterUserUseCase = Depends(get_register_use_case)  #  Ahora depende de una función
):
    user = register_use_case.execute(auth_request)
    if not user:
        raise HTTPException(status_code=400, detail="Error al registrar usuario")
    return user

@router.post("/login", response_model=AuthResponse)
def login(
    auth_request: AuthRequest,
    login_use_case: LoginUseCase = Depends(get_login_use_case)  #  Ahora depende de una función
):
    user = login_use_case.execute(auth_request)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user
