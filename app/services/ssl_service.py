import ssl
import socket

def get_ssl_info(hostname):

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:

        with context.wrap_socket(
            sock,
            server_hostname=hostname
        ) as secure_sock:

            cert = secure_sock.getpeercert()

    return {
        "subject": cert.get("subject"),
        "issuer": cert.get("issuer"),
        "version": cert.get("version"),
        "expires": cert.get("notAfter")
    }
