from fastapi import FastAPI
from app.database.connection import engine
from app.api.models.tablas import Base
from app.api.endpoints.endpoints import rutas

from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

#Crear las tablas de sql desde python
Base.metadata.create_all(bind=engine)

#Variable para administrar la aplicacion
app=FastAPI()

#Configurar el protocolo CORS   
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Activar EL API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)