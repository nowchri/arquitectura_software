# app/api/estudiante_bastidor.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
import app
from app.models.estudiante_bastidor import EstudianteBastidor
from app.schemas.estudiante_bastidor import EstudianteBastidorOut, EstudianteBastidorCreate

router = APIRouter(prefix="/estudiante-bastidor", tags=["Estudiante-Bastidor"])

# GET: Todos los registros
@router.get("/", response_model=list[EstudianteBastidorOut])
def obtener_relaciones(db: Session = Depends(get_db)):
    return db.query(EstudianteBastidor).options(
        joinedload(EstudianteBastidor.estudiante),
        joinedload(EstudianteBastidor.bastidor)
    ).all()
# POST: Asociar un estudiante con un bastidor
@router.post("/")
def asociar_estudiante_bastidor(
    relacion_: EstudianteBastidorCreate,
    db: Session = Depends(get_db)
):
    # Verificar que el estudiante exista
    estudiante_existe = db.query(db.query(app.models.estudiante.Estudiante.id_estudiante).filter_by(id_estudiante=relacion_.id_estudiante).exists()).scalar()
    if not estudiante_existe:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # Verificar que el bastidor exista
    bastidor_existe = db.query(db.query(app.models.bastidor.Bastidor.id_bastidor).filter_by(id_bastidor=relacion_.id_bastidor).exists()).scalar()
    if not bastidor_existe:
        raise HTTPException(status_code=404, detail="Bastidor no encontrado")

    # Evitar duplicados
    existe = db.query(EstudianteBastidor).filter_by(
        id_estudiante=relacion_.id_estudiante,
        id_bastidor=relacion_.id_bastidor
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="La relación ya existe")

    nueva_relacion = EstudianteBastidor(
        id_estudiante=relacion_.id_estudiante,
        id_bastidor=relacion_.id_bastidor
    )

    db.add(nueva_relacion)
    db.commit()
    db.refresh(nueva_relacion)

    return {
        "mensaje": "Estudiante asociado con bastidor",
        "id_registro": nueva_relacion.id_registro_eb,
        "id_estudiante": relacion_.id_estudiante,
        "id_bastidor": relacion_.id_bastidor
    }

# DELETE: Eliminar la asociación
@router.delete("/{id_registro_eb}")
def eliminar_asociacion(id_registro_eb: int, db: Session = Depends(get_db)):
    relacion = db.query(EstudianteBastidor).filter(EstudianteBastidor.id_registro_eb == id_registro_eb).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")

    db.delete(relacion)
    db.commit()

    return {"mensaje": "Asociación eliminada correctamente"}