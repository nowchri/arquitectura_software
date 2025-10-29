# app/strategies/generador_reporte.py
from abc import ABC, abstractmethod
from typing import Dict
from fpdf import FPDF

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
    
class PDFBuilder(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Reporte de Pagos por Mes", ln=True, align="C")

    def tabla_pagos(self, filas):
        headers = ["Estudiante", "Doc. Identidad", "Tipo", "Monto", "Fecha", "Método", "Detalle"]
        col_widths = [28, 30, 22, 24, 28, 26, 34]  # Nombre de Estudiante mucho más estrecho
        self.set_font("Arial", "B", 10)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 9, h, border=1, align="C")
        self.ln()
        self.set_font("Arial", "", 9)
        for pago in filas:
            # Obtén sólo el primer nombre y primer apellido
            nombre_completo = pago["nombre_estudiante"]
            partes = nombre_completo.split()
            primer_nombre = partes[0] if len(partes) > 0 else ""
            primer_apellido = partes[1] if len(partes) > 1 else ""
            nombre_corto = f"{primer_nombre} {primer_apellido}".strip()

            contenido = [
                nombre_corto,  # Solo primer nombre y apellido
                str(pago["documento_identidad"]),
                str(pago["tipo"]),
                f"{pago['monto']:.2f}",
                str(pago["fecha"]),
                str(pago["metodo_pago"]),
                str(pago["detalle"])
            ]
            for i, valor in enumerate(contenido):
                self.cell(col_widths[i], 8, valor, border=1)
            self.ln()


def generar_pdf_pagos(filas):
    pdf = PDFBuilder('P', 'mm', 'A4')
    pdf.add_page()
    pdf.tabla_pagos(filas)
    pdf_bytes = pdf.output(dest="S")
    # Si pdf_bytes es bytearray, conviértelo a bytes
    if isinstance(pdf_bytes, bytearray):
        pdf_bytes = bytes(pdf_bytes)
    elif isinstance(pdf_bytes, str):
        pdf_bytes = pdf_bytes.encode('latin1')
    return pdf_bytes