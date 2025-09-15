from abc import ABC, abstractmethod

class EstrategiaPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        pass

class NequiPago(EstrategiaPago):
    def procesar_pago(self, monto: float) -> bool:
        print(f"Procesando pago de {monto} COP con Nequi")
        return True

class EfectivoPago(EstrategiaPago):
    def procesar_pago(self, monto: float) -> bool:
        print(f"Pago en efectivo de {monto} COP registrado")
        return True