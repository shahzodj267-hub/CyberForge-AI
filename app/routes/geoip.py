from fastapi import APIRouter
from app.services.geoip_service import get_ip_info

router = APIRouter()

@router.get("/ip/{ip}")
def ip_lookup(ip: str):

    try:

        return get_ip_info(ip)

    except Exception as e:

        return {
            "error": str(e)
        }
