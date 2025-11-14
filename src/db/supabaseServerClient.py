from supabase import create_client
import os

# 1. Variables de Entorno (Se cargan directamente desde Vercel)
# Usamos un nombre diferente para las constantes a nivel de módulo
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_ROLE_KEY") 
# Nota: La función get_supabase_client usará estas constantes.


# 2. Función de inyección de dependencia (para usar con FastAPI Depends)
# Esto asegura que el cliente SOLO se inicialice cuando se llama a una ruta.
def get_supabase_client():
    # Es crucial que las variables tengan valor. Si no, Vercel falla.
    if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
        # Aunque las revisamos, dejamos esta excepción para depuración
        raise RuntimeError("Faltan o están vacías las credenciales de Supabase. Revisa Vercel Environment Variables.")
        
    # Inicializa el cliente solo dentro de la función
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# 3. ELIMINAR O COMENTAR LA LÍNEA QUE CREA EL CLIENTE INMEDIATAMENTE:
# # supabasee = create_client(supabase_url, supabase_service_key)