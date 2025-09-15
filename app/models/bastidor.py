# app/models/bastidor.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Bastidor(Base):
    __tablename__ = "bastidor"

    id_bastidor = Column(Integer, primary_key=True, autoincrement=True)
    medidas = Column(String(50), nullable=False)
    precio = Column(Float(precision=2), nullable=False)

    estudiantes = relationship("EstudianteBastidor", back_populates="bastidor")
    pagos = relationship("Pago", back_populates="bastidor")