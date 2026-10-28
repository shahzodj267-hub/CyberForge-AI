from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.routers.auth import get_current_user
from app.crud.user import User

router = APIRouter(
    prefix="/ai",
    tags=["AI Analysis Module"],
    dependencies=[Depends(get_current_user)]
)

class AIQueryRequest(BaseModel):
    prompt: str
    context_data: str = None

@router.post("/analyze")
def analyze_security_event(query: AIQueryRequest):
    prompt_lower = query.prompt.lower()
    
    # AI tahlil simulyatsiyasi (kelgusida mahalliy LLM / Ollama yoki OpenAI API ga ulanadi)
    if "ip" in prompt_lower or "shubhali" in prompt_lower:
        analysis = "AI Analysis: The provided IP exhibits characteristics of automated scanning or reconnaissance activity. High request frequency detected from a non-residential ASN."
        remediation = "Block the IP at the firewall level and monitor adjacent assets for lateral movement."
    elif "login" in prompt_lower or "attack" in prompt_lower or "brute" in prompt_lower:
        analysis = "AI Analysis: Detected pattern matches a credential stuffing or brute-force attack vector against authentication endpoints."
        remediation = "Enforce rate limiting, implement account lockout policies after 5 failed attempts, and require MFA."
    else:
        analysis = f"AI Analysis: Processed security query successfully for context: '{query.prompt}'."
        remediation = "Maintain standard monitoring protocols and ensure system logs are forwarded to the SIEM."

    return {
        "status": "success",
        "model": "CyberForge-AI-LLM-v1",
        "query": query.prompt,
        "ai_analysis": analysis,
        "remediation_steps": remediation
    }
