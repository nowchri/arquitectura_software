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

class UsuarioConcreto:
    def __init__(self, user_obj, rol_impl):
        self.id_usuario = user_obj.id_usuario
        self.nombre = user_obj.nombre
        self.apellido = user_obj.apellido
        self.rol = rol_impl
        self.correo_electronico = user_obj.correo_electronico
        self.contrasena = user_obj.contrasena

    def iniciar_sesion(self, password):
        return self.contrasena == password

    def tiene_permiso(self, permiso):
        return self.rol.tiene_permiso(permiso)

class UsuarioProxy:
    def __init__(self, usuario_real):
        self._usuario_real = usuario_real
        self._estado_cuenta = "activo"  # puedes expandir esto

    def iniciar_sesion(self, password):
        # Aquí puedes añadir lógica extra: logging, bloquear tras 3 fallos, etc
        return self._usuario_real.iniciar_sesion(password)

    def tiene_permiso(self, permiso):
        return self._usuario_real.tiene_permiso(permiso)