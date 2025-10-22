# app/api/estudiantes.py
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.estudiante import Estudiante
from app.schemas.estudiante import EstudianteCreate, EstudianteOut

router = APIRouter()

# GET: Obtener todos los estudiantes
@router.get("/estudiantes/", response_model=List[EstudianteOut])
def obtener_estudiantes(documento: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Estudiante)
    if documento:
        query = query.filter(Estudiante.documento_identidad == documento)
    return query.all()

# POST: Crear un nuevo estudiante
@router.post("/estudiantes/")
def crear_estudiante(estudiante_: EstudianteCreate, db: Session = Depends(get_db)):
    existe_correo = db.query(Estudiante).filter(Estudiante.correo_electronico == estudiante_.correo_electronico).first()
    existe_doc = db.query(Estudiante).filter(Estudiante.documento_identidad == estudiante_.documento_identidad).first()
    if existe_correo:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    if existe_doc:
        raise HTTPException(status_code=400, detail="El documento ya está registrado")
    nuevo_estudiante = Estudiante(**estudiante_.dict())
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return {"mensaje": "Estudiante creado", "id_estudiante": nuevo_estudiante.id_estudiante}