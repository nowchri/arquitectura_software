# app/schemas/estudiante.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class EstudianteCreate(BaseModel):
    documento_identidad: str
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[str] = None
    telefono: str
    correo_electronico: str
    estado: str = "Inactivo"
    fecha_inscripcion: date
    id_plan: Optional[int] = None

class EstudianteOut(BaseModel):
    id_estudiante: int
    documento_identidad: str
    nombre: str
    apellido: str
    telefono: str
    correo_electronico: str
    estado: str
    fecha_inscripcion: date

    class Config:
        orm_mode = True

class EstudianteUpdate(BaseModel):
    documento_identidad: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    correo_electronico: Optional[str] = None
    estado: Optional[str] = None