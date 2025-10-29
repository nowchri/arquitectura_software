# app/schemas/clase.py
from pydantic import BaseModel
from datetime import datetime

class ClaseCreate(BaseModel):
    nombre: str
    fecha_hora: str  # Formato ISO: "2023-11-01T10:00:00"
    contador_clase: int
    id_plan: int
    id_estudiante: int

class ClaseUpdate(BaseModel):
    nombre: str = None
    fecha_hora: str = None
    contador_clase: int = None
    id_plan: int = None
    id_estudiante: int = None