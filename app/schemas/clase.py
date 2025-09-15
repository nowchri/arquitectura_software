# app/schemas/clase.py
"""
from pydantic import BaseModel

class ClaseSchema(BaseModel):
    id_clase: int
    nombre: str
    fecha_hora: str
    contador_clase: int
    id_plan: int
    id_estudiante: int
"""
# app/schemas/clase.py
from pydantic import BaseModel

class ClaseCreate(BaseModel):
    nombre: str
    fecha_hora: str  # Formato ISO: "2023-11-01T10:00:00"
    contador_clase: int
    id_plan: int
    id_estudiante: int
