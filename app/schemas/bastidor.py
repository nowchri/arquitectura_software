# app/schemas/bastidor.py
from pydantic import BaseModel

class BastidorCreate(BaseModel):
    medidas: str
    precio: float

class BastidorUpdate(BaseModel):
    medidas: str = None
    precio: float = None