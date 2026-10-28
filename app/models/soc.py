from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database.database import Base

class LogModel(Base):
    __tablename__ = "soc_logs"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String, index=True)
    event_type = Column(String, index=True)
    description = Column(Text)
    severity = Column(String, default="low")
    timestamp = Column(DateTime, default=datetime.utcnow)

class AlertModel(Base):
    __tablename__ = "soc_alerts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    source_ip = Column(String, index=True)
    severity = Column(String, default="high")
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
