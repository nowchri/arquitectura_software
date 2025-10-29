# app/models/rol_implementacion.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class RolImplementacion(Base):
    __tablename__ = "rol_implementacion"

    rol_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_rol = Column(String(100), nullable=False)
    
    usuarios = relationship("Usuario", back_populates="rol")

class RolImplementacionBase:
    def tiene_permiso(self, permiso: str) -> bool:
        raise NotImplementedError

    def get_nombre_rol(self):
        raise NotImplementedError

class RolAdministrador(RolImplementacionBase):
    def tiene_permiso(self, permiso):
        # El admin puede todo, puedes personalizar esto según permisos específicos
        return True
    def get_nombre_rol(self):
        return "Administrador"

class RolDocente(RolImplementacionBase):
    def tiene_permiso(self, permiso):
        # Definir permisos específicos para docentes
        return permiso in ["ver_estudiantes", "gestionar_clases"]  # Ejemplo
    def get_nombre_rol(self):
        return "Docente"