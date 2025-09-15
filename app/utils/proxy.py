# app/utils/proxy.py
from abc import ABC, abstractmethod

class RolImplementacion(ABC):
    @abstractmethod
    def tiene_permiso(self, permiso: str) -> bool:
        pass

    @abstractmethod
    def get_nombre_rol(self) -> str:
        pass

class RolDocente(RolImplementacion):
    def tiene_permiso(self, permiso: str) -> bool:
        permisos = ["registrar_asistencia", "ver_clases"]
        return permiso in permisos

    def get_nombre_rol(self) -> str:
        return "docente"

class RolAdministrador(RolImplementacion):
    def tiene_permiso(self, permiso: str) -> bool:
        return True

    def get_nombre_rol(self) -> str:
        return "administrador"