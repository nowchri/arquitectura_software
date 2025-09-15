# app/models/redencion.py
from sqlalchemy import Column, Integer, ForeignKey, Date, String, Text, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class RedencionDeClaseNoAsistida(Base):
    __tablename__ = "redencion_de_clase_no_asistida"

    id_redencion = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    id_clase_original = Column(Integer, ForeignKey("clase.id_clase"))
    fecha = Column(Date, nullable=False)
    estado_redencion = Column(String(20), default="pendiente")
    motivo = Column(Text)

    estudiante = relationship("Estudiante", back_populates="redenciones")
    clase_original = relationship("Clase", back_populates="redenciones")

    __table_args__ = (
        CheckConstraint("estado_redencion IN ('pendiente', 'aprobada', 'rechazada')", name="estado_redencion_check"),
    )