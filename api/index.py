from fastapi import FastAPI, Request
from src.middleware.verificarToken import VerificarToken
from src.routes.login import Login, LoginData
from src.routes.registrar import Registrar, RegisterData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "API de Login",
    description = "Permite gestionar el Auth de usuarios",
    version = "2.0.0",
    contact = {
        "name": "Carlos Pinto",
        "email": "cpinto5@udi.edu.co",
    },
    swagger_ui_parameters={
        "displayRequestDuration": True,      # Muestra tiempo de respuesta
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", description="Página principal del backend para validar si está funcionando.")
def estado():
    return {"message": "🚀 Backend de Login activo"}

#@app.get("/verify", description="Para validar el JWT del usuario.")
#def verificar_token_endpoint(request: Request):
#    return VerificarToken(request)

@app.post("/login", description="Para validar las credenciales del usuario.")
def login_endpoint(login_data: LoginData):
    return Login(login_data)

@app.post("/registrar", description="Para registrar un usuario en el Auth de Supabase.")
def registrar_brigadista_endpoint(register_data: RegisterData):
    return Registrar(register_data)
