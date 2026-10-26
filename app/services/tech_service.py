import requests

def detect_technologies(domain):

    response = requests.get(
        f"https://{domain}",
        timeout=10
    )

    headers = response.headers

    detected = []

    server = headers.get("Server", "")

    if "nginx" in server.lower():
        detected.append("Nginx")

    if "apache" in server.lower():
        detected.append("Apache")

    if "cloudflare" in server.lower():
        detected.append("Cloudflare")

    html = response.text.lower()

    if "wp-content" in html:
        detected.append("WordPress")

    if "react" in html:
        detected.append("React")

    if "next" in html:
        detected.append("Next.js")

    return detected
