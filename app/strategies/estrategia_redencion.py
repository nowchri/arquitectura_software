# app/strategies/estrategia_redencion.py
from abc import ABC, abstractmethod


class EstrategiaRedencion(ABC):
    """
    Interfaz base para todas las estrategias de redención de faltas.
    """
    @abstractmethod
    def aplicar_redencion(self, id_estudiante: str, id_clase: str) -> dict:
        pass


class RedencionJustificacion(EstrategiaRedencion):
    """
    Redención mediante justificación médica o familiar.
    """
    def aplicar_redencion(self, id_estudiante: str, id_clase: str) -> dict:
        return {
            "tipo": "justificacion",
            "estado": "aprobado",
            "mensaje": f"Redención aplicada para el estudiante {id_estudiante} (clase {id_clase}) por justificación."
        }


class RedencionAsistenciaFutura(EstrategiaRedencion):
    """
    Redención mediante asistencia extra en otra clase.
    """
    def aplicar_redencion(self, id_estudiante: str, id_clase: str) -> dict:
        return {
            "tipo": "asistencia_futura",
            "estado": "pendiente",
            "mensaje": f"Estudiante {id_estudiante} debe asistir a una clase extra para redimir la falta."
        }


class RedencionEventoInstitucional(EstrategiaRedencion):
    """
    Redención por participación en evento institucional.
    """
    def aplicar_redencion(self, id_estudiante: str, id_clase: str) -> dict:
        return {
            "tipo": "evento_institucional",
            "estado": "aprobado",
            "mensaje": f"Redención automática para {id_estudiante} por participación en evento."
        }