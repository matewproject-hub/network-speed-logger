from supabase import create_client
from dotenv import load_dotenv
import os
from pathlib import Path


# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")       # Add this to .env
SUPABASE_KEY = os.getenv("SUPABASE_KEY")       # Add this to .env
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

