# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 CAMBIA ESTAS CREDENCIALES POR LAS TUYAS (sin acentos ni caracteres especiales)
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/ACADEMIA_ARTE"

# Crear motor de conexión
engine = create_engine(DATABASE_URL)

# Configurar sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()