# app/services/pago_service.py
from app.models.pago import Pago
from app.strategies.estrategia_pago import EstrategiaPago, NequiPago, EfectivoPago
from sqlalchemy.orm import Session

def procesar_pago(db: Session, id_estudiante: int, tipo: str, monto: float, fecha: str, metodo_pago: str, id_bastidor: int = None, id_plan: int = None):
    # Seleccionar estrategia
    estrategias = {
        "nequi": NequiPago(),
        "efectivo": EfectivoPago()
    }
    estrategia = estrategias.get(metodo_pago.lower())
    if not estrategia:
        raise ValueError("Método de pago no soportado")

    # Procesar pago
    try:
        resultado = estrategia.procesar_pago(monto)
    except Exception as e:
        estado = "fallido"
        raise ValueError(f"Error al procesar pago: {str(e)}")
    else:
        estado = "completado"

    # Crear registro en DB
    nuevo_pago = Pago(
        id_estudiante=id_estudiante,
        tipo=tipo,
        monto=monto,
        fecha=fecha,
        metodo_pago=metodo_pago,
        estado=estado,
        id_bastidor=id_bastidor,
        id_plan=id_plan
    )

    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)

    return nuevo_pago