# app/models/usuario.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    rol_id = Column(Integer, ForeignKey("rol_implementacion.rol_id"), nullable=False)

    rol = relationship("RolImplementacion", back_populates="usuarios")