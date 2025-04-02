# src/database.py
from supabase import create_client, Client
from . import config  # Relative import

def get_supabase_client() -> Client:
    try:
        return create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    except Exception as e:
        print(f"Error connecting to Supabase: {e}")
        raise

def fetch_data(table_name: str) -> list:
    try:
        supabase = get_supabase_client()
        response = supabase.table(table_name).select('*').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
        return []