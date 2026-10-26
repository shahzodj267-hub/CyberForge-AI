from fastapi import APIRouter

from app.services.security_headers_service import (
    check_security_headers
)

router = APIRouter()

@router.get("/security-headers/{domain}")
def security_headers(domain: str):

    try:

        return {
            "domain": domain,
            "security_headers":
                check_security_headers(domain)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
