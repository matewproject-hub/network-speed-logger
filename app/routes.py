from fastapi import APIRouter
from app.database import supabase
from datetime import datetime

router = APIRouter()

@router.get("/logs")
def get_logs():
    return (
        supabase
        .table("speedlogs")
        .select("*")
        .order("timestamp", desc=True)
        .execute()
        .data
    )



    res = supabase.table("speedlogs").insert(data).execute()
    return res.data
