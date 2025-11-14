from fastapi import FastAPI
from contexts.access_management.application.controllers import auth_controller
from contexts.patient_management.application.controllers import patient_controller
from contexts.doctor_management.application.controllers.doctor_controller import router as doctor_router
from dotenv import load_dotenv
from middleware.error_handler import custom_error_handler

load_dotenv()  # Cargar variables de entorno al iniciar la app

app = FastAPI(title="Backend con FastAPI y Firebase")

# Agregar middleware de manejo de errores
app.add_exception_handler(Exception, custom_error_handler)

# Registrar rutas
app.include_router(auth_controller.router)

# Registrar rutas de Patient Management
app.include_router(patient_controller.router)

app.include_router(doctor_router)

print("Rutas de Patient Management registradas correctamente")

# Imprimir rutas para depuración
print("Rutas registradas en FastAPI:")
for route in app.routes:
    print(route.__dict__['path'])

# Mensaje de bienvenida
@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}

# Imprimir rutas registradas
print("\n Rutas registradas en FastAPI:")
for route in app.routes:
    print(f"{route.__dict__['path']} - {route.__dict__['methods']}")

