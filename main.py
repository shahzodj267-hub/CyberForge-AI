from fastapi import FastAPI
import dns.resolver

app = FastAPI(
    title="CyberForge AI",
    version="0.0.1"
)

@app.get("/")
def home():
    return {
        "project": "CyberForge AI",
        "status": "running"
    }


@app.get("/dns/{domain}")
def dns_lookup(domain: str):

    records = []

    try:
        answers = dns.resolver.resolve(domain, "A")

        for rdata in answers:
            records.append(str(rdata))

    except Exception as e:
        return {"error": str(e)}

    return {
        "domain": domain,
        "a_records": records
    }
