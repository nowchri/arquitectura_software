# app/api/clases.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.clase import Clase
from app.schemas.clase import ClaseCreate

router = APIRouter()

# GET: Todas las clases
@router.get("/clases/")
def obtener_clases(db: Session = Depends(get_db)):
    return db.query(Clase).all()

# POST: Nueva clase
@router.post("/clases/")
def crear_clase(clase_: ClaseCreate, db: Session = Depends(get_db)):
    # Verificar que el estudiante y plan existan (opcional)
    nueva_clase = Clase(**clase_.dict())
    db.add(nueva_clase)
    db.commit()
    db.refresh(nueva_clase)
    return {"mensaje": "Clase creada", "id_clase": nueva_clase.id_clase}