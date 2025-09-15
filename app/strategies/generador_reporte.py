# app/strategies/generador_reporte.py
from abc import ABC, abstractmethod
from typing import Dict


class GeneradorReporte(ABC):
    """
    Interfaz base para generar reportes en diferentes formatos.
    """
    @abstractmethod
    def generar(self, data: Dict) -> str:
        pass


class PDFGenerator(GeneradorReporte):
    """
    Genera un reporte en formato PDF.
    """
    def generar(self, data: Dict) -> str:
        # Simulación de generación de PDF
        contenido = f"""
        REPORTE EN PDF
        Tipo: {data.get('tipo')}
        Fecha: {data.get('fecha')}
        Contenido: {data.get('contenido')}
        Firmado digitalmente.
        """
        return contenido.strip()


class ExcelGenerator(GeneradorReporte):
    """
    Genera un reporte en formato Excel (.xlsx).
    """
    def generar(self, data: Dict) -> str:
        # Simulación de generación de Excel
        contenido = f"""
        REPORTE EN EXCEL
        Tipo: {data.get('tipo')}
        Fecha: {data.get('fecha')}
        Filas: {len(data.get('contenido', []))}
        Exportado a hoja de cálculo.
        """
        return contenido.strip()