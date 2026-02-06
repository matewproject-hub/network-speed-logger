from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

from app.routes import router
from app.database import engine
from app.models import Base
from app.speedtest_service import run_speedtest

app = FastAPI()

app.include_router(router)

# Create tables
Base.metadata.create_all(bind=engine)

# Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(run_speedtest, "interval", hours=1)
scheduler.start()

@app.get("/")
def home():
    return {"message": "Speed Logger API running"}
