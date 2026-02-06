🚀 Network Speed Logger with Cloud Storage

A full-stack network monitoring system that periodically measures internet speed and securely stores results in the cloud for visualization and analysis.

This project was built to demonstrate practical skills in network diagnostics, backend automation, cloud databases, and API-driven dashboards.

📌 Problem Statement

Internet connectivity issues are often difficult to diagnose without historical data.

Most users rely on manual speed tests which provide only momentary snapshots.

This project solves that by:

Automatically logging network speed at fixed intervals

Persisting results in a cloud database

Providing a dashboard to visualize performance over time

✅ Features

Automated speed testing (download / upload / ping)

Scheduled background logging

PostgreSQL cloud storage (Supabase)

REST API built with FastAPI

Data retention policy (auto cleanup after 7 days)

Frontend dashboard for viewing results

Deployed backend and frontend

Swagger API documentation

🧠 Architecture
Frontend (HTML + JS + Chart.js)
            ↓
        FastAPI Backend
            ↓
      Speedtest Engine
            ↓
     Supabase PostgreSQL

🛠 Tech Stack
Backend

Python 3.10+

FastAPI

Speedtest-cli

SQLAlchemy

APScheduler

PostgreSQL (Supabase)

Frontend

HTML

JavaScript (Fetch API)

Chart.js

Cloud

Supabase (Database)

Render (Backend deployment)

Vercel (Frontend deployment)

📂 Project Structure
network-speed-logger/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md

⚙️ How It Works

Backend scheduler runs speed tests every fixed interval (1 minute for testing / 1 hour in production)

Results are stored in Supabase PostgreSQL

Old records are automatically deleted after 7 days

Frontend fetches data from API

Dashboard displays logs and charts
