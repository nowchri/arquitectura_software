# app/services/reporte_service.py
from sqlalchemy.orm import Session
from app.models.pago import Pago
from app.models.estudiante import Estudiante
from app.models.bastidor import Bastidor
from app.models.plan_de_clases import PlanDeClases
from datetime import date
from app.strategies.generador_reporte import PDFGenerator, ExcelGenerator

def obtener_pagos_del_mes(db: Session, anio: int, mes: int):
    pagos = (
        db.query(Pago)
        .join(Estudiante, Pago.id_estudiante == Estudiante.id_estudiante)
        .outerjoin(Bastidor, Pago.id_bastidor == Bastidor.id_bastidor)
        .outerjoin(PlanDeClases, Pago.id_plan == PlanDeClases.id_plan)
        .filter(Pago.fecha >= date(anio, mes, 1))
        .filter(Pago.fecha < date(anio, mes + 1 if mes < 12 else anio + 1, 1))
        .filter(Pago.estado == "completado")  # Opcional, solo pagos completados
        .all()
    )

    resultado = []
    for pago in pagos:
        fila = {
            "nombre_estudiante": pago.estudiante.nombre + " " + pago.estudiante.apellido,
            "documento_identidad": pago.estudiante.documento_identidad,
            "tipo": pago.tipo,
            "monto": pago.monto,
            "fecha": pago.fecha.strftime("%Y-%m-%d"),
            "metodo_pago": pago.metodo_pago,
        }
        # Lógica por tipo
        if pago.tipo == "bastidor":
            fila["detalle"] = pago.bastidor.medidas if pago.bastidor else "N/A"
        elif pago.tipo == "mensualidad":
            fila["detalle"] = pago.plan.nombre if pago.plan else "N/A"
        elif pago.tipo == "inscripcion":
            fila["detalle"] = "N/A"
        resultado.append(fila)
    return resultado

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