# app/schemas/estudiante_bastidor.py

from pydantic import BaseModel
from typing import Optional
from app.schemas.estudiante import EstudianteOut
from app.schemas.bastidor import BastidorOut

# Para crear una nueva relación
class EstudianteBastidorCreate(BaseModel):
    id_estudiante: int
    id_bastidor: int

# Para leer una relación (con datos del estudiante y bastidor)
class EstudianteBastidorOut(BaseModel):
    id_registro_eb: int
    id_estudiante: int
    id_bastidor: int
    estudiante: Optional[EstudianteOut] = None
    bastidor: Optional[BastidorOut] = None

    class Config:
        from_attributes = True  # ← Reemplaza orm_mode=True