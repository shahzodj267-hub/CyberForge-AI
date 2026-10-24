from fastapi import FastAPI
import dns.resolver
import whois
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
@app.get("/whois/{domain}")
def whois_lookup(domain: str):

    try:
        data = whois.whois(domain)

        return {
            "domain": domain,
            "registrar": str(data.registrar),
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
        }

    except Exception as e:
        return {"error": str(e)}
