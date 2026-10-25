import requests

def get_headers(domain):

    url = f"https://{domain}"

    response = requests.get(
        url,
        timeout=10
    )

    return dict(response.headers)
