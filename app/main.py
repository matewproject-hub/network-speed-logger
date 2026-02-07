import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler

from app.routes import router
from app.speedtest_service import run_speedtest

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

# Initialize scheduler
scheduler = BackgroundScheduler()

# Fetch SUPABASE_URL at runtime
SUPABASE_URL = os.environ.get("SUPABASE_URL")
if not SUPABASE_URL:
    raise RuntimeError("SUPABASE_URL not set in environment variables!")

@app.on_event("startup")
def startup_event():
    # Run the first speedtest immediately
    run_speedtest(supabase_url=SUPABASE_URL)
    
    # Schedule subsequent runs every 60 minutes
    scheduler.add_job(run_speedtest, "interval", minutes=60, args=[SUPABASE_URL])
    scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()

@app.get("/")
def root():
    return {"status": "Network Speed Logger API running"}
