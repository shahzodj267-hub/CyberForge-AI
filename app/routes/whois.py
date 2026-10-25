from fastapi import APIRouter
from app.services.whois_service import get_whois

router = APIRouter()

@router.get("/whois/{domain}")
def whois_lookup(domain: str):

    try:

        return get_whois(domain)

    except Exception as e:

        return {
            "error": str(e)
        }
