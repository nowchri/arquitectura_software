# app/api/pagos.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.services.pago_service import procesar_pago
from pydantic import BaseModel
from app.models.pago import Pago
from app.models.estudiante import Estudiante
from app.models.plan_de_clases import PlanDeClases
from app.models.bastidor import Bastidor

router = APIRouter()

class PagoCreate(BaseModel):
    id_estudiante: int
    tipo: str
    monto: float
    fecha: str
    metodo_pago: str
    id_bastidor: int = None
    id_plan: int = None
    
@router.get("/pagos/")
def obtener_pagos(documento: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(Pago).join(Estudiante)
    if documento:
        query = query.filter(Estudiante.documento_identidad == documento)
    pagos = query.options(
        joinedload(Pago.estudiante),
        joinedload(Pago.plan),
        joinedload(Pago.bastidor)
    ).all()

    resultado = []
    for p in pagos:
        resultado.append({
            "id_pago": p.id_pago,
            "tipo": p.tipo,
            "monto": p.monto,
            "fecha": str(p.fecha),
            "metodo_pago": p.metodo_pago,
            "estado": p.estado,
            "id_bastidor": p.id_bastidor,
            "id_plan": p.id_plan,
            "documento_estudiante": p.estudiante.documento_identidad,
            "nombre_estudiante": f"{p.estudiante.nombre} {p.estudiante.apellido}",
            "bastidor_medidas": p.bastidor.medidas if p.bastidor else None,
            "plan_nombre": p.plan.nombre if p.plan else None,
            "plan_numero_clases": p.plan.numero_de_clases_mes if p.plan else None,
        })
    return resultado

@router.post("/pagos/")
def crear_pago(pago_data: PagoCreate, db: Session = Depends(get_db)):
    try:
        resultado = procesar_pago(
            db=db,
            id_estudiante=pago_data.id_estudiante,
            tipo=pago_data.tipo,
            monto=pago_data.monto,
            fecha=pago_data.fecha,
            metodo_pago=pago_data.metodo_pago,
            id_bastidor=pago_data.id_bastidor,
            id_plan=pago_data.id_plan
        )
        return {"mensaje": "Pago registrado", "id_pago": resultado.id_pago}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))