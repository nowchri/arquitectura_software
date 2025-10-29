# app/api/clases.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.clase import Clase
from app.models.estudiante import Estudiante
from app.models.plan_de_clases import PlanDeClases
from app.schemas.clase import ClaseCreate, ClaseUpdate

router = APIRouter(prefix="/clases", tags=["Clases"])

# GET: Todas las clases
@router.get("/")
def obtener_clases(db: Session = Depends(get_db)):
    return db.query(Clase).all()

# POST: Nueva clase
@router.post("/")
def crear_clase(clase_: ClaseCreate, db: Session = Depends(get_db)):
    # Verificar que el estudiante exista
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == clase_.id_estudiante).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # Verificar que el plan exista
    plan = db.query(PlanDeClases).filter(PlanDeClases.id_plan == clase_.id_plan).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan de clases no encontrado")

    nueva_clase = Clase(**clase_.dict())
    db.add(nueva_clase)
    db.commit()
    db.refresh(nueva_clase)
    return {"mensaje": "Clase creada", "id_clase": nueva_clase.id_clase}

# PUT: Actualizar clase
@router.put("/{id_clase}")
def actualizar_clase(id_clase: int, clase_: ClaseUpdate, db: Session = Depends(get_db)):
    clase = db.query(Clase).filter(Clase.id_clase == id_clase).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")

    datos_actualizados = clase_.dict(exclude_unset=True)

    # Validar estudiante si se cambia
    if "id_estudiante" in datos_actualizados:
        estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == datos_actualizados["id_estudiante"]).first()
        if not estudiante:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # Validar plan si se cambia
    if "id_plan" in datos_actualizados:
        plan = db.query(PlanDeClases).filter(PlanDeClases.id_plan == datos_actualizados["id_plan"]).first()
        if not plan:
            raise HTTPException(status_code=404, detail="Plan de clases no encontrado")

    for key, value in datos_actualizados.items():
        setattr(clase, key, value)

    db.commit()
    db.refresh(clase)
    return {"mensaje": "Clase actualizada", "clase": clase}

# DELETE: Eliminar clase
@router.delete("/{id_clase}")
def eliminar_clase(id_clase: int, db: Session = Depends(get_db)):
    clase = db.query(Clase).filter(Clase.id_clase == id_clase).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")

    db.delete(clase)
    db.commit()
    return {"mensaje": "Clase eliminada correctamente"}