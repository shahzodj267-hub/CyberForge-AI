import dns.resolver

def get_a_records(domain):

    records = []

    answers = dns.resolver.resolve(domain, "A")

    for rdata in answers:
        records.append(str(rdata))

    return records
