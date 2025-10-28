# app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import Base, engine

# Importa los modelos para que SQLAlchemy los reconozca
from app.models import Estudiante, Clase, Pago, Asistencia, RedencionDeClaseNoAsistida
<<<<<<< Updated upstream

from app.api import estudiantes, clases, pagos, asistencias, redenciones, reportes, login
=======
>>>>>>> Stashed changes

from app.api import estudiantes, clases, pagos, asistencias, redenciones, reportes, login
from app.api import bastidores
# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Academia de Arte API", version="1.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Incluir rutas
app.include_router(login.router, prefix="/api")
app.include_router(estudiantes.router, prefix="/api")
app.include_router(clases.router, prefix="/api")
app.include_router(pagos.router, prefix="/api")
app.include_router(asistencias.router, prefix="/api")
app.include_router(redenciones.router, prefix="/api")
<<<<<<< Updated upstream
app.include_router(reportes.router, prefix="/api")
=======
app.include_router(reportes.router, prefix="/api")
app.include_router(bastidores.router, prefix="/api")  # ← Añade esta línea
>>>>>>> Stashed changes
