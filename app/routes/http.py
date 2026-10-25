from fastapi import APIRouter
from app.services.http_service import get_headers

router = APIRouter()

@router.get("/headers/{domain}")
def headers_lookup(domain: str):

    try:

        return {
            "domain": domain,
            "headers": get_headers(domain)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
