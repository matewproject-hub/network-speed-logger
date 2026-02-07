from fastapi import APIRouter
from app.database import supabase

router = APIRouter()

@router.get("/logs")
def get_logs():
    res = (
        supabase
        .table("speedlogs")
        .select("*")
        .order("timestamp", desc=True)
        .execute()
    )

    return res.data


