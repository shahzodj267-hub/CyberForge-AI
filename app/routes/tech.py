from fastapi import APIRouter
from app.services.tech_service import (
    detect_technologies
)

router = APIRouter()

@router.get("/tech/{domain}")
def tech_lookup(domain: str):

    try:

        return {
            "domain": domain,
            "technologies":
                detect_technologies(domain)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
