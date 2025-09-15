# app/api/pagos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.pago_service import procesar_pago
from pydantic import BaseModel
from app.models.pago import Pago

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
def obtener_pagos(db: Session = Depends(get_db)):
    return db.query(Pago).all()

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