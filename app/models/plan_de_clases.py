# app/models/plan_de_clases.py
from sqlalchemy import Column, Integer, String, Text, Float, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base  # o app.database según tu estructura

class PlanDeClases(Base):
    __tablename__ = "plan_de_clases"

    id_plan = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    numero_de_clases_mes = Column(Integer, nullable=False)
    precio_mensualidad = Column(Float(precision=2), nullable=False)

    # Relaciones inversas
    estudiantes = relationship("Estudiante", back_populates="plan")
    clases = relationship("Clase", back_populates="plan")
    pagos = relationship("Pago", back_populates="plan")