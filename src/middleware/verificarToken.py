from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from src.db.supabaseServerClient import get_supabase_client

def VerificarToken(request: Request):
    try:
        auth_header = request.headers.get("authorization")
        token = auth_header.split(" ")[1] if auth_header else None
        if not token:
            raise HTTPException(status_code=401, detail="Token requerido")

        response = get_supabase_client().auth.get_user(token)
        
        # Accede directamente a los atributos del objeto response
        if response.user is None:
            raise HTTPException(status_code=403, detail="Token inválido")

        return {
            "valido": True,
            "usuario": {
                "id": response.user.id,
                "email": response.user.email,
            }
        }
    except HTTPException as e:
        raise e
    except Exception as err:
        print("Error: ", err)

        if "Invalid" in str(err) or "invalid" in str(err):
            raise HTTPException(status_code=403, detail="Token inválido")
        
        return JSONResponse(status_code=500, content={"error": "Error en el servidor"})
