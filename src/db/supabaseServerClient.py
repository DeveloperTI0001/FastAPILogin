from supabase import create_client
import os

supabase_url = os.getenv("SUPABASE_URL")
supabase_service_key = os.getenv("SUPABASE_ROLE_KEY")

supabasee = create_client(supabase_url, supabase_service_key)