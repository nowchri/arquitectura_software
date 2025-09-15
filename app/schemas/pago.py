# app/schemas/pago.py
from pydantic import BaseModel

class PagoSchema(BaseModel):
    id_pago: int
    id_estudiante: int
    tipo: str
    monto: float
    fecha: str
    metodo_pago: str
    estado: str
    id_bastidor: int
    id_plan: int