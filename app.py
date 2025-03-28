from fastapi import FastAPI
from contexts.access_management.application.controllers import auth_controller

app = FastAPI(title="Backend con FastAPI y Firebase")

# Registrar rutas
app.include_router(auth_controller.router)

# Mensaje de bienvenida
@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}
