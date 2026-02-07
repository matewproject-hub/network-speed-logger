from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from apscheduler.schedulers.background import BackgroundScheduler
from app.speedtest_service import run_speedtest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

run_speedtest()

scheduler = BackgroundScheduler()
scheduler.add_job(run_speedtest, "interval", hours=1)
scheduler.start()


@app.get("/")
def root():
    return {"status": "Network Speed Logger API running"}
