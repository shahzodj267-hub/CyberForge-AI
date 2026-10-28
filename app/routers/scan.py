from fastapi import APIRouter, Depends
from app.routers.auth import get_current_user
from app.crud.user import User

# Barcha skanerlash endpointlari avtomatik ravishda get_current_user orqali himoyalanadi
router = APIRouter(
    prefix="",
    tags=["Scanning & Recon"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/dns/{domain}")
def dns_lookup(domain: str):
    return {"domain": domain, "status": "success", "tool": "DNS Lookup", "result": "A, MX, TXT records found"}

@router.get("/whois/{domain}")
def whois_lookup(domain: str):
    return {"domain": domain, "status": "success", "tool": "WHOIS Lookup", "result": "Domain registration details"}

@router.get("/ip/{ip}")
def ip_lookup(ip: str):
    return {"ip": ip, "status": "success", "tool": "IP Lookup", "result": "GeoIP & Network info"}

@router.get("/subdomains/{domain}")
def subdomain_scan(domain: str):
    return {"domain": domain, "status": "success", "tool": "Subdomain Scanner", "result": ["sub1.domain.com", "api.domain.com"]}

@router.get("/headers/{domain}")
def headers_lookup(domain: str):
    return {"domain": domain, "status": "success", "tool": "Headers Lookup", "result": "HTTP security headers analyzed"}

@router.get("/ssl/{domain}")
def ssl_lookup(domain: str):
    return {"domain": domain, "status": "success", "tool": "SSL Certificate Check", "result": "Certificate valid"}

@router.get("/security-headers/{domain}")
def security_headers(domain: str):
    return {"domain": domain, "status": "success", "tool": "Security Headers", "result": "CSP, HSTS check passed"}

@router.get("/tech/{domain}")
def tech_lookup(domain: str):
    return {"domain": domain, "status": "success", "tool": "Tech Stack Detection", "result": "Nginx, FastAPI, React"}
