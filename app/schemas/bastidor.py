# app/schemas/bastidor.py

from pydantic import BaseModel
from typing import Optional

class BastidorCreate(BaseModel):
    medidas: str
    precio: float

class BastidorOut(BaseModel):
    id_bastidor: int
    medidas: str
    precio: float

    class Config:
        from_attributes = True  # Reemplaza orm_mode=True en Pydantic v2

class BastidorUpdate(BaseModel):
    medidas: Optional[str] = None
    precio: Optional[float] = None