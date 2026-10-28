from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.routers.auth import get_current_user
from app.models.soc import LogModel, AlertModel

router = APIRouter(
    prefix="/soc",
    tags=["SOC Module"],
    dependencies=[Depends(get_current_user)]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LogEntry(BaseModel):
    source_ip: str
    event_type: str
    description: str
    severity: str = "low"

@router.post("/ingest-log")
def ingest_log(log: LogEntry, db: Session = Depends(get_db)):
    # Logni bazaga yozish
    db_log = LogModel(
        source_ip=log.source_ip,
        event_type=log.event_type,
        description=log.description,
        severity=log.severity
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    # Brute-force urinishlarini bazadan tekshirish
    failed_count = db.query(LogModel).filter(
        LogModel.source_ip == log.source_ip,
        LogModel.event_type == "login_failed"
    ).count()

    alert_triggered = False
    current_alert = None

    if failed_count >= 3:
        # Alert allaqachon bormi tekshiramiz
        existing_alert = db.query(AlertModel).filter(
            AlertModel.source_ip == log.source_ip,
            AlertModel.title == "Brute Force Attack Detected!"
        ).first()

        if not existing_alert:
            alert_triggered = True
            db_alert = AlertModel(
                title="Brute Force Attack Detected!",
                source_ip=log.source_ip,
                severity="high",
                message=f"Multiple failed login attempts ({failed_count}) detected from IP {log.source_ip}"
            )
            db.add(db_alert)
            db.commit()
            db.refresh(db_alert)
            current_alert = {
                "alert_id": db_alert.id,
                "title": db_alert.title,
                "source_ip": db_alert.source_ip,
                "severity": db_alert.severity,
                "message": db_alert.message
            }
        else:
            current_alert = {
                "alert_id": existing_alert.id,
                "title": existing_alert.title,
                "source_ip": existing_alert.source_ip,
                "severity": existing_alert.severity,
                "message": existing_alert.message
            }

    return {
        "status": "success",
        "message": "Log successfully ingested and saved to PostgreSQL database",
        "alert_triggered": alert_triggered,
        "alert": current_alert
    }

@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(AlertModel).all()
    return alerts

@router.get("/timeline")
def get_incident_timeline(db: Session = Depends(get_db)):
    logs = db.query(LogModel).order_by(LogModel.timestamp.desc()).limit(10).all()
    total_logs = db.query(LogModel).count()
    total_alerts = db.query(AlertModel).count()

    return {
        "status": "success",
        "total_logs": total_logs,
        "total_alerts": total_alerts,
        "timeline": logs
    }
