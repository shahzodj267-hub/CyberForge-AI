import dns.resolver
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(target):

    try:
        dns.resolver.resolve(target, "A")
        return target

    except:
        return None


def discover_subdomains(domain):

    found = []

    with open("wordlists/common.txt") as file:
        subdomains = file.read().splitlines()

    targets = [
        f"{sub}.{domain}"
        for sub in subdomains
    ]

    with ThreadPoolExecutor(max_workers=20) as executor:

        results = executor.map(
            check_subdomain,
            targets
        )

    for result in results:

        if result:
            found.append(result)

    return found
