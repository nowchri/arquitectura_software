# app/models/asistencia.py
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Date, String, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Asistencia(Base):
    __tablename__ = "asistencia"

    id_asistencia = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    id_clase = Column(Integer, ForeignKey("clase.id_clase"))
    asistio = Column(Boolean, default=False, nullable=False)
    jornada = Column(String(10), nullable=False)
    fecha = Column(Date, nullable=False)

    estudiante = relationship("Estudiante", back_populates="asistencias")
    clase = relationship("Clase", back_populates="asistencias")

    __table_args__ = (
        CheckConstraint("jornada IN ('mañana', 'tarde', 'noche')", name="jornada_check"),
    )