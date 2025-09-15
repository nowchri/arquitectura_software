# app/api/asistencias.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.asistencia import Asistencia
from app.schemas.asistencia import AsistenciaCreate

router = APIRouter()

# GET: Todas las asistencias
@router.get("/asistencias/")
def obtener_asistencias(db: Session = Depends(get_db)):
    return db.query(Asistencia).all()

# POST: Registrar asistencia
@router.post("/asistencias/")
def crear_asistencia(asistencia_: AsistenciaCreate, db: Session = Depends(get_db)):
    # Validar jornada
    if asistencia_.jornada not in ["mañana", "tarde", "noche"]:
        raise HTTPException(status_code=400, detail="Jornada inválida")

    nueva_asistencia = Asistencia(**asistencia_.dict())
    db.add(nueva_asistencia)
    db.commit()
    db.refresh(nueva_asistencia)
    return {"mensaje": "Asistencia registrada", "id_asistencia": nueva_asistencia.id_asistencia}