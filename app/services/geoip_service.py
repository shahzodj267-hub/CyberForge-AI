import requests

def get_ip_info(ip):

    response = requests.get(
        f"http://ip-api.com/json/{ip}",
        timeout=10
    )

    data = response.json()

    return {
        "ip": ip,
        "country": data.get("country"),
        "city": data.get("city"),
        "isp": data.get("isp"),
        "org": data.get("org")
    }
