# app/api/redenciones.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.redencion import RedencionDeClaseNoAsistida
from app.schemas.redencion import RedencionCreate

router = APIRouter()

# GET: Todas las redenciones
@router.get("/redenciones/")
def obtener_redenciones(db: Session = Depends(get_db)):
    return db.query(RedencionDeClaseNoAsistida).all()

# POST: Solicitar redención
@router.post("/redenciones/")
def crear_redencion(redencion_: RedencionCreate, db: Session = Depends(get_db)):
    if redencion_.estado_redencion not in ["pendiente", "aprobada", "rechazada"]:
        raise HTTPException(status_code=400, detail="Estado de redención inválido")

    nueva_redencion = RedencionDeClaseNoAsistida(**redencion_.dict())
    db.add(nueva_redencion)
    db.commit()
    db.refresh(nueva_redencion)
    return {"mensaje": "Redención creada", "id_redencion": nueva_redencion.id_redencion}