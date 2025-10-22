# app/models/estudiante.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Estudiante(Base):
    __tablename__ = "estudiante"

    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    documento_identidad = Column(String(20), nullable=False, unique=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    fecha_nacimiento = Column(Date)
    telefono = Column(String(20), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    estado = Column(String(10), default="Inactivo")
    fecha_inscripcion = Column(Date, nullable=False)
    id_plan = Column(Integer, ForeignKey("plan_de_clases.id_plan"))

    plan = relationship("PlanDeClases", back_populates="estudiantes")
    clases = relationship("Clase", back_populates="estudiante")
    pagos = relationship("Pago", back_populates="estudiante")
    bastidores = relationship("EstudianteBastidor", back_populates="estudiante")
    asistencias = relationship("Asistencia", back_populates="estudiante")
    redenciones = relationship("RedencionDeClaseNoAsistida", back_populates="estudiante")

    __table_args__ = (
        CheckConstraint("estado IN ('Activo', 'Inactivo')", name="estado_check"),
    )