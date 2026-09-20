"""RDAP domain availability adapter.

v0.4 foundation: keeps provider-specific logic isolated.
"""

import json
import urllib.request

RDAP_SERVERS = {
    "com": "https://rdap.verisign.com/com/v1/domain/",
    "net": "https://rdap.verisign.com/net/v1/domain/",
}


def query(domain: str):
    tld = domain.split(".")[-1]
    base = RDAP_SERVERS.get(tld)
    if not base:
        return {"domain": domain, "status": "UNSUPPORTED"}

    try:
        with urllib.request.urlopen(base + domain, timeout=5) as r:
            data = json.loads(r.read().decode())
        return {"domain": domain, "status": "REGISTERED", "name": data.get("ldhName")}
    except Exception:
        return {"domain": domain, "status": "NOT_FOUND_OR_UNKNOWN"}
