from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.database import Base

class SpeedLog(Base):
    __tablename__ = "speedlogs"

    id = Column(Integer, primary_key=True, index=True)
    download = Column(Float)
    upload = Column(Float)
    ping = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
