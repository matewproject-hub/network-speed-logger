import speedtest
from datetime import datetime, timedelta
from app.database import supabase

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)

    data = {
        "download": download,
        "upload": upload,
        "ping": ping,
        "timestamp": datetime.utcnow().isoformat()
    }

    supabase.table("speedlogs").insert(data).execute()

    # cleanup older than 7 days
    cutoff = (datetime.utcnow() - timedelta(days=7)).isoformat()

    supabase.table("speedlogs").delete().lt("timestamp", cutoff).execute()

    print("✅ Speedtest logged")

