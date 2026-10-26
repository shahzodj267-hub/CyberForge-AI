from fastapi import FastAPI

from app.routes.dns import router as dns_router
from app.routes.whois import router as whois_router
from app.routes.geoip import router as geoip_router
from app.routes.subdomain import router as subdomain_router
from app.routes.http import router as http_router
from app.routes.ssl import router as ssl_router
from app.routes.security_headers import (
    router as security_headers_router
)
from app.routes.tech import router as tech_router

app = FastAPI(
    title="CyberForge AI",
    version="0.0.1"
)

app.include_router(dns_router)
app.include_router(whois_router)
app.include_router(geoip_router)
app.include_router(subdomain_router)
app.include_router(http_router)
app.include_router(ssl_router)
app.include_router(
    security_headers_router
)
app.include_router(tech_router)

@app.get("/")
def home():
    return {
        "project": "CyberForge AI",
        "status": "running"
    }

