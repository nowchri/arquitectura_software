# app/api/reportes.py
from fastapi import APIRouter, Depends, Response
from app.services.reporte_service import obtener_pagos_del_mes
from app.strategies.generador_reporte import generar_pdf_pagos
from app.database import get_db

router = APIRouter()

@router.get("/reportes/pagos/pdf/")
def exportar_pagos_pdf(anio: int, mes: int, db=Depends(get_db)):
    pagos = obtener_pagos_del_mes(db, anio, mes)
    pdf_binario = generar_pdf_pagos(pagos)
    # Debe ser content=pdf_binario, NO solo pdf_binario!
    return Response(content=pdf_binario, media_type="application/pdf",
                    headers={"Content-Disposition": "attachment; filename=pagos_reporte.pdf"})