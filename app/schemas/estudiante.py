# app/schemas/estudiante.py
from pydantic import BaseModel
from typing import Optional

class EstudianteCreate(BaseModel):
    documento_identidad: str
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[str] = None
    telefono: str
    correo_electronico: str
    estado: str = "Inactivo"
    fecha_inscripcion: str
    id_plan: int

class EstudianteOut(BaseModel):
    id_estudiante: int
    documento_identidad: str
    nombre: str
    apellido: str
    telefono: str
    correo_electronico: str
    estado: str

    class Config:
        orm_mode = True