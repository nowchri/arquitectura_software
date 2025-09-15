# app/api/estudiantes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.estudiante import Estudiante
from app.schemas.estudiante import EstudianteCreate

router = APIRouter()

# GET: Obtener todos los estudiantes
@router.get("/estudiantes/")
def obtener_estudiantes(db: Session = Depends(get_db)):
    return db.query(Estudiante).all()

# POST: Crear un nuevo estudiante
@router.post("/estudiantes/")
def crear_estudiante(estudiante_: EstudianteCreate, db: Session = Depends(get_db)):
    # Verificar que el correo no exista
    existe = db.query(Estudiante).filter(Estudiante.correo_electronico == estudiante_.correo_electronico).first()
    if existe:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    nuevo_estudiante = Estudiante(**estudiante_.dict())
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return {"mensaje": "Estudiante creado", "id_estudiante": nuevo_estudiante.id_estudiante}