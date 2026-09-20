"""
BrandForge domain scanner foundation.

Checks DNS availability locally and provides extension points
for RDAP/WHOIS providers.
"""

import socket

EXTENSIONS = [
    ".com",
    ".ai",
    ".dev",
    ".io",
    ".tech",
    ".systems",
]


def dns_exists(domain: str) -> bool:
    try:
        socket.gethostbyname(domain)
        return True
    except OSError:
        return False


def scan_name(name: str):
    results = []
    for ext in EXTENSIONS:
        domain = name.lower() + ext
        results.append(
            {
                "domain": domain,
                "dns": dns_exists(domain),
            }
        )
    return results


if __name__ == "__main__":
    for item in scan_name("synora"):
        print(item)
