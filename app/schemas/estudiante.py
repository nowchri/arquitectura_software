# app/schemas/estudiante.py
from pydantic import BaseModel

class EstudianteCreate(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: str = None
    telefono: str
    correo_electronico: str
    estado: str = "Inactivo"
    fecha_inscripcion: str
    id_plan: int