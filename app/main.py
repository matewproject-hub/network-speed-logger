from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler

from app.routes import router
from app.speedtest_service import run_speedtest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():

    run_speedtest()

    scheduler.add_job(run_speedtest, "interval", minutes=60)
    scheduler.start()

@app.get("/")
def root():
    return {"status": "Network Speed Logger API running"}
