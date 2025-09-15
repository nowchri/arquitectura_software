# app/api/reportes.py
"""from fastapi import APIRouter
from app.services.reporte_service import generar_reporte_asistencia_pdf

router = APIRouter()

@router.get("/reportes/asistencia/pdf")
def reporte_asistencia_pdf():
    contenido = generar_reporte_asistencia_pdf()
    return {"formato": "PDF", "contenido": contenido}

"""
# app/api/reportes.py
from fastapi import APIRouter
from app.services.reporte_service import generar_reporte_asistencia

router = APIRouter()

@router.get("/reportes/asistencia/pdf")
def reporte_asistencia_pdf():
    contenido = generar_reporte_asistencia("pdf")
    return {"formato": "PDF", "reporte": contenido}