from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.db.supabaseServerClient import supabasee
from pydantic import BaseModel
from typing import Dict, Optional

class RegisterData(BaseModel):
    correo: str
    contraseña: Optional[str] = None
    user_metadata: Dict = {}
    app_metadata: Dict = {}

def Registrar(register_data: RegisterData):
    try:
        correo = register_data.correo
        contraseña = register_data.contraseña
        user_metadata = register_data.user_metadata
        app_metadata = register_data.app_metadata

        if not correo or not contraseña:
            raise HTTPException(status_code=400, detail="Correo y contraseña requeridos")

        response = supabasee.auth.admin.create_user(
            {
                "email": correo.strip().lower(),
                "password": contraseña,
                "user_metadata": user_metadata,
                "app_metadata": app_metadata
            }
        )

        return {
            "message": "Usuario creado con éxito.",
            "user": response.user,
        }
    
    except HTTPException as e:
        raise e
    except Exception as err:
        print("Error: ", err)
        error_str = str(err)

        if "already exists" in error_str.lower() or "duplicate" in error_str.lower():
            raise HTTPException(status_code=409, detail="El correo ya está registrado")
        
        return JSONResponse(status_code=500, content={"error": str(err)})