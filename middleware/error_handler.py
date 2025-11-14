from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import firebase_admin


async def custom_error_handler(request: Request, exc: Exception):
    """ Middleware para manejar errores globales. """

    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail},
        )

    if isinstance(exc, firebase_admin.exceptions.FirebaseError):
        return JSONResponse(
            status_code=500,
            content={"error": "Error en Firebase", "details": str(exc)},
        )

    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor", "details": str(exc)},
    )
