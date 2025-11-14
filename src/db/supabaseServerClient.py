from supabase import create_client
import os

supabase_url = os.getenv("SUPABASE_URL") or "https://rnmkcfdwaaeqpbepdstq.supabase.co"
supabase_service_key = os.getenv("SUPABASE_ROLE_KEY") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJubWtjZmR3YWFlcXBiZXBkc3RxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Njg3MTYxMywiZXhwIjoyMDcyNDQ3NjEzfQ.bIBqv0y332Pn_ZZHfAYlv8sYoG0HJL8pwbk1x1WmQFE"

if not supabase_url or not supabase_service_key:
    raise Exception("Faltan credenciales de Supabase en el entorno.")

supabasee = create_client(supabase_url, supabase_service_key)