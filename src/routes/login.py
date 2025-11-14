from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from src.db.supabaseServerClient import supabasee
from pydantic import BaseModel

class LoginData(BaseModel):
    email: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "martin5435412@gmail.com",
                    "password": "123456"
                }
            ]
        }
    }

def Login(request: Request):
    try:
        email = request.email.strip().lower()
        password = request.password
        if not email or not password:
            raise HTTPException(status_code=400, detail="Email y password requeridos")

        response = supabasee.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        return {
            "message": "Inicio de sesión exitoso",
            "session": response.session,
            "user": response.user,
        }
    
    except HTTPException as e:
        raise e
    except Exception as err:
        if "Invalid login credentials" in str(err):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
        return JSONResponse(status_code=500, content={"error": "Error en el servidor"})