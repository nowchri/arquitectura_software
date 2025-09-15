
# app/schemas/redencion.py
from pydantic import BaseModel

class RedencionCreate(BaseModel):
    id_estudiante: int
    id_clase_original: int
    fecha: str
    motivo: str
    estado_redencion: str = "pendiente"  # por defecto