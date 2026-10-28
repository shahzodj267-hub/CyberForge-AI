from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import auth, scan, threat, soc, ai, report
from app.models import soc as soc_model  # SOC modellarini import qilish

# Ma'lumotlar bazasi jadvallarini yaratish (shu jumladan yangi soc_logs va soc_alerts)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CyberForge AI",
    version="0.0.1",
    description="Advanced Automated Vulnerability Scanner & Red Team Dashboard"
)

# Barcha routerlarni to'liq ulash
app.include_router(auth.router)
app.include_router(scan.router)
app.include_router(threat.router)
app.include_router(soc.router)
app.include_router(ai.router)
app.include_router(report.router)

@app.get("/", tags=["Home"])
def read_root():
    return {"message": "Welcome to CyberForge-AI API. Database persistence and all modules are active!"}
