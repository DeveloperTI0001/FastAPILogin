from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.db.supabaseServerClient import supabasee
from pydantic import BaseModel
from typing import Dict, Optional

class uuid(BaseModel):
    uuid: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uuid": "715ed5db-f090-4b8c-a067-640ecee36aa0",
                }
            ]
        }
    }


def EliminarUsuario(request: uuid):
    try:
        uuid = request.uuid

        if not uuid:
            raise HTTPException(status_code=400, detail="uuid del usuario en Auth requerido")

        supabasee.auth.admin.delete_user(uuid)

        return {
            "message": "Usuario eliminado con éxito.",
        }
    
    except HTTPException as e:
        raise e
    except Exception as err:
        print("Error: ", err)

        return JSONResponse(status_code=500, content={"error": str(err)})