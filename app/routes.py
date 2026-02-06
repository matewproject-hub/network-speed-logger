from fastapi import APIRouter
from app.database import SessionLocal
from app.models import SpeedLog

router = APIRouter()

@router.get("/")
def root():
    return {"status": "Network Speed Logger running"}

@router.get("/logs")
def get_logs():
    db = SessionLocal()
    logs = db.query(SpeedLog).order_by(SpeedLog.created_at.desc()).all()
    db.close()
    return logs
