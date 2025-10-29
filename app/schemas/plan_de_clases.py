# app/schemas/plan_de_clases.py
from pydantic import BaseModel

class PlanDeClasesCreate(BaseModel):
    nombre: str
    descripcion: str = None
    numero_de_clases_mes: int
    precio_mensualidad: float

class PlanDeClasesUpdate(BaseModel):
    nombre: str = None
    descripcion: str = None
    numero_de_clases_mes: int = None
    precio_mensualidad: float = None