# app/schemas/asistencia.py
from pydantic import BaseModel

class AsistenciaCreate(BaseModel):
    id_estudiante: int
    id_clase: int
    asistio: bool
    jornada: str  # "mañana", "tarde", "noche"
    fecha: str    # "2023-11-01"