from fastapi import APIRouter
from app.services.ssl_service import get_ssl_info

router = APIRouter()

@router.get("/ssl/{domain}")
def ssl_lookup(domain: str):

    try:

        return get_ssl_info(domain)

    except Exception as e:

        return {
            "error": str(e)
        }
