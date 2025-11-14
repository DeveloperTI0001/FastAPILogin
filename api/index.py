from fastapi import FastAPI, Request
# ELIMINAR ESTA LÍNEA, YA NO ES NECESARIA CON MANGUM:
# from asgiref.wsgi import WsgiToAsgi
from mangum import Mangum

from src.middleware.verificarToken import VerificarToken
from src.routes.login import Login, LoginData
from src.routes.registrar import Registrar, RegisterData
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends
from src.db.supabaseServerClient import get_supabase_client # Supongamos que aquí pones tu función

app = FastAPI(
    title="API de Login",
    description="Permite gestionar el Auth de usuarios",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def estado():
    return {"message": "🚀 Backend de Login activo"}

@app.get("/verify")
def verificar_token_endpoint(request: Request):
    # Asegúrate de que esta función no accede al cliente de Supabase al inicio
    return VerificarToken(request)

@app.post("/login")
# Si Login() requiere el cliente de Supabase, debes usar Depends aquí:
def login_endpoint(login_data: LoginData):
    return Login(login_data)

@app.post("/registrar")
def registrar_endpoint(register_data: RegisterData):
    return Registrar(register_data)

# Adaptador para serverless (Vercel / AWS Lambda)
handler = Mangum(app)