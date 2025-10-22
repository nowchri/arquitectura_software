# app/api/estudiantes.py
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.estudiante import Estudiante
from app.schemas.estudiante import EstudianteCreate, EstudianteOut, EstudianteUpdate

router = APIRouter()

# GET: Obtener todos los estudiantes
@router.get("/estudiantes/", response_model=List[EstudianteOut])
def obtener_estudiantes(documento: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Estudiante)
    if documento:
        query = query.filter(Estudiante.documento_identidad == documento)
    return query.all()

# GET: Obtener un estudiante por DOCUMENTO
@router.get("/estudiantes/perfil/{documento}", response_model=EstudianteOut)
def obtener_estudiante(documento: str, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.documento_identidad == documento).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

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

# PUT: Actualizar estudiante por documento
@router.put("/estudiantes/{documento}", response_model=EstudianteOut)
def actualizar_estudiante(documento: str, estudiante_: EstudianteUpdate, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.documento_identidad == documento).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    # Validar email único si se cambia
    if estudiante_.correo_electronico and estudiante_.correo_electronico != estudiante.correo_electronico:
        existe_correo = db.query(Estudiante).filter(Estudiante.correo_electronico == estudiante_.correo_electronico).first()
        if existe_correo:
            raise HTTPException(status_code=400, detail="El correo ya está registrado")
    
    # Validar documento único si se cambia
    if estudiante_.documento_identidad and estudiante_.documento_identidad != estudiante.documento_identidad:
        existe_doc = db.query(Estudiante).filter(Estudiante.documento_identidad == estudiante_.documento_identidad).first()
        if existe_doc:
            raise HTTPException(status_code=400, detail="El documento ya está registrado")
    
    # Actualizar campos
    for key, value in estudiante_.dict(exclude_unset=True).items():
        setattr(estudiante, key, value)
    
    db.commit()
    db.refresh(estudiante)
    return estudiante