# app/models/rol_implementacion.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class RolImplementacion(Base):
    __tablename__ = "rol_implementacion"

    rol_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_rol = Column(String(100), nullable=False)
    
    usuarios = relationship("Usuario", back_populates="rol")