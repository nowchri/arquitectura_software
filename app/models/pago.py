# app/models/pago.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Pago(Base):
    __tablename__ = "pago"

    id_pago = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiante.id_estudiante"))
    tipo = Column(String(20), nullable=False)
    monto = Column(Float(precision=2), nullable=False)
    fecha = Column(Date, nullable=False)
    metodo_pago = Column(String(50))
    estado = Column(String(20), default="pendiente")
    id_bastidor = Column(Integer, ForeignKey("bastidor.id_bastidor"))
    id_plan = Column(Integer, ForeignKey("plan_de_clases.id_plan"))

    estudiante = relationship("Estudiante", back_populates="pagos")
    bastidor = relationship("Bastidor", back_populates="pagos")
    plan = relationship("PlanDeClases", back_populates="pagos")

    __table_args__ = (
        CheckConstraint("tipo IN ('inscripcion', 'mensualidad', 'bastidor')", name="tipo_check"),
        CheckConstraint("estado IN ('pendiente', 'completado', 'fallido')", name="estado_pago_check"),
    )