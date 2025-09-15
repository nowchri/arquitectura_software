# app/models/estudiante_bastidor.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EstudianteBastidor(Base):
    __tablename__ = "estudiante_bastidor"

    id_registro_eb = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"), nullable=False)
    id_bastidor = Column(Integer, ForeignKey("bastidor.id_bastidor"), nullable=False)

    estudiante = relationship("Estudiante", back_populates="bastidores")
    bastidor = relationship("Bastidor", back_populates="estudiantes")