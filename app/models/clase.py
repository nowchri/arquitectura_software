# app/models/clase.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Clase(Base):
    __tablename__ = "clase"

    id_clase = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    contador_clase = Column(Integer, nullable=False)
    id_plan = Column(Integer, ForeignKey("plan_de_clases.id_plan"))
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))

    plan = relationship("PlanDeClases", back_populates="clases")
    estudiante = relationship("Estudiante", back_populates="clases")
    asistencias = relationship("Asistencia", back_populates="clase")
    redenciones = relationship("RedencionDeClaseNoAsistida", back_populates="clase_original")