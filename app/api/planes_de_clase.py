# app/api/planes_de_clase.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.plan_de_clases import PlanDeClases
from app.schemas.plan_de_clases import PlanDeClasesCreate, PlanDeClasesUpdate

router = APIRouter(prefix="/planes-de-clase", tags=["Planes de Clase"])

# GET: Todos los planes
@router.get("/")
def obtener_planes(db: Session = Depends(get_db)):
    return db.query(PlanDeClases).all()

# POST: Nuevo plan
@router.post("/")
def crear_plan(plan_: PlanDeClasesCreate, db: Session = Depends(get_db)):
    # Verificar que no exista un plan con el mismo nombre
    existe = db.query(PlanDeClases).filter(PlanDeClases.nombre == plan_.nombre).first()
    if existe:
        raise HTTPException(status_code=400, detail="Ya existe un plan con este nombre")

    nuevo_plan = PlanDeClases(**plan_.dict())
    db.add(nuevo_plan)
    db.commit()
    db.refresh(nuevo_plan)
    return {"mensaje": "Plan creado", "id_plan": nuevo_plan.id_plan}

# PUT: Actualizar plan
@router.put("/{id_plan}")
def actualizar_plan(id_plan: int, plan_: PlanDeClasesUpdate, db: Session = Depends(get_db)):
    plan = db.query(PlanDeClases).filter(PlanDeClases.id_plan == id_plan).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")

    # Evitar duplicados en nombre si se cambia
    if plan_.nombre is not None and plan_.nombre != plan.nombre:
        ya_existe = db.query(PlanDeClases).filter(PlanDeClases.nombre == plan_.nombre).first()
        if ya_existe:
            raise HTTPException(status_code=400, detail="Ya existe un plan con ese nombre")

    datos_actualizados = plan_.dict(exclude_unset=True)
    for key, value in datos_actualizados.items():
        setattr(plan, key, value)

    db.commit()
    db.refresh(plan)
    return {"mensaje": "Plan actualizado", "plan": plan}

# DELETE: Eliminar plan
@router.delete("/{id_plan}")
def eliminar_plan(id_plan: int, db: Session = Depends(get_db)):
    plan = db.query(PlanDeClases).filter(PlanDeClases.id_plan == id_plan).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")

    # ⚠️ No permitir eliminación si tiene estudiantes asociados
    if len(plan.estudiantes) > 0:
        raise HTTPException(
            status_code=400,
            detail="No se puede eliminar el plan porque tiene estudiantes inscritos"
        )

    db.delete(plan)
    db.commit()
    return {"mensaje": "Plan eliminado correctamente"}