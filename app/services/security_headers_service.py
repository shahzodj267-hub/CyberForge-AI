import requests

def check_security_headers(domain):

    url = f"https://{domain}"

    response = requests.get(
        url,
        timeout=10
    )

    headers = response.headers

    return {
        "HSTS":
            "Strict-Transport-Security" in headers,

        "CSP":
            "Content-Security-Policy" in headers,

        "X-Frame-Options":
            "X-Frame-Options" in headers,

        "X-Content-Type-Options":
            "X-Content-Type-Options" in headers,

        "Referrer-Policy":
            "Referrer-Policy" in headers,

        "Permissions-Policy":
            "Permissions-Policy" in headers
    }
