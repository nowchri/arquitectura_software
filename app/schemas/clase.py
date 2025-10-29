# app/schemas/clase.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ClaseCreate(BaseModel):
    nombre: str
    fecha_hora: str  # Formato ISO: "2023-11-01T10:00:00"
    contador_clase: int = 1
    id_plan: Optional[int] = None
    id_estudiante: Optional[int] = None

    class Config:
        from_attributes = True

class ClaseUpdate(BaseModel):
    nombre: str = None
    fecha_hora: str = None
    contador_clase: int = None
    id_plan: int = None
    id_estudiante: int = None