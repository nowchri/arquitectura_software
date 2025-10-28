# app/api/bastidores.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.bastidor import Bastidor
from app.schemas.bastidor import BastidorCreate, BastidorUpdate

router = APIRouter(prefix="/bastidores", tags=["Bastidores"])

# GET: Todos los bastidores
@router.get("/")
def obtener_bastidores(db: Session = Depends(get_db)):
    return db.query(Bastidor).all()

# POST: Nuevo bastidor
@router.post("/")
def crear_bastidor(bastidor_data: BastidorCreate, db: Session = Depends(get_db)):
    nuevo_bastidor = Bastidor(**bastidor_data.dict())
    db.add(nuevo_bastidor)
    db.commit()
    db.refresh(nuevo_bastidor)
    return {"mensaje": "Bastidor creado", "id_bastidor": nuevo_bastidor.id_bastidor}

# PUT: Actualizar bastidor
@router.put("/{id_bastidor}")
def actualizar_bastidor(id_bastidor: int, bastidor_data: BastidorUpdate, db: Session = Depends(get_db)):
    bastidor = db.query(Bastidor).filter(Bastidor.id_bastidor == id_bastidor).first()
    if not bastidor:
        raise HTTPException(status_code=404, detail="Bastidor no encontrado")

    datos_actualizados = bastidor_data.dict(exclude_unset=True)
    for key, value in datos_actualizados.items():
        setattr(bastidor, key, value)

    db.commit()
    db.refresh(bastidor)
    return {"mensaje": "Bastidor actualizado", "bastidor": bastidor}

# DELETE: Eliminar bastidor
@router.delete("/{id_bastidor}")
def eliminar_bastidor(id_bastidor: int, db: Session = Depends(get_db)):
    bastidor = db.query(Bastidor).filter(Bastidor.id_bastidor == id_bastidor).first()
    if not bastidor:
        raise HTTPException(status_code=404, detail="Bastidor no encontrado")

    db.delete(bastidor)
    db.commit()
    return {"mensaje": "Bastidor eliminado correctamente"}git