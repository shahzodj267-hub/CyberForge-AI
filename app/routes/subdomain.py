from fastapi import APIRouter
from app.services.subdomain_service import discover_subdomains

router = APIRouter()

@router.get("/subdomains/{domain}")
def subdomain_scan(domain: str):

    try:

        results = discover_subdomains(domain)

        return {
            "domain": domain,
            "found": results
        }

    except Exception as e:

        return {
            "error": str(e)
        }
