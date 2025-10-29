# app/api/login.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario, UsuarioConcreto, UsuarioProxy
from app.models.rol_implementacion import RolAdministrador

router = APIRouter()

@router.post("/login-admin")
def login_admin(data: dict, db: Session = Depends(get_db)):
    email = data.get("email")
    password = data.get("password")

    user = db.query(Usuario).filter(Usuario.correo_electronico == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos (usr)")

    # Busca si es admin
    rol_obj = user.rol
    if rol_obj.nombre_rol.lower() != "administrador":
        raise HTTPException(status_code=403, detail="Solo los administradores pueden ingresar aquí")
    
    # Aplica estructura proxy
    usuario_concreto = UsuarioConcreto(user, RolAdministrador())
    proxy = UsuarioProxy(usuario_concreto)

    if not proxy.iniciar_sesion(password):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos (pwd)")

    return {"success": True, "nombre": user.nombre, "rol": "Administrador"}