from fastapi import APIRouter
from app.services.dns_service import get_a_records

router = APIRouter()

@router.get("/dns/{domain}")
def dns_lookup(domain: str):

    try:
        records = get_a_records(domain)

        return {
            "domain": domain,
            "a_records": records
        }

    except Exception as e:
        return {
            "error": str(e)
        }
