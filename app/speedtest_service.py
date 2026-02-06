import speedtest
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import SpeedLog

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    db: Session = SessionLocal()

    log = SpeedLog(
        download=round(download, 2),
        upload=round(upload, 2),
        ping=round(ping, 2)
    )

    db.add(log)
    db.commit()

    # delete logs older than 7 days
    cutoff = datetime.utcnow() - timedelta(days=7)
    db.query(SpeedLog).filter(SpeedLog.created_at < cutoff).delete()
    db.commit()

    db.close()

    print("✅ Speedtest logged")
