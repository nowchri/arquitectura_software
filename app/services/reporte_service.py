# app/services/reporte_service.py
from app.strategies.generador_reporte import PDFGenerator, ExcelGenerator

def generar_reporte_asistencia(formato: str = "pdf"):
    data = {
        "tipo": "asistencia",
        "fecha": "2025-04-05",
        "detalle": [
            {"estudiante": "E001", "clase": "Dibujo", "asistio": True},
            {"estudiante": "E002", "clase": "Pintura", "asistio": False}
        ]
    }

    if formato == "pdf":
        generador = PDFGenerator()
    elif formato == "excel":
        generador = ExcelGenerator()
    else:
        raise ValueError("Formato no soportado")

    return generador.generar(data)