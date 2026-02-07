import os
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from app.routes import router
from app.speedtest_service import run_speedtest

app = FastAPI()
scheduler = BackgroundScheduler()
app.include_router(router)

@app.on_event("startup")
def startup_event():
    # Fetch secrets at runtime
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("Supabase secrets not found!")

    # First speedtest run
    run_speedtest(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
    
    # Schedule subsequent runs every 60 minutes
    scheduler.add_job(
        run_speedtest,
        "interval",
        minutes=60,
        args=[SUPABASE_URL, SUPABASE_KEY]
    )
    scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
