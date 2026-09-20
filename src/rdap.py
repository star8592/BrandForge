"""RDAP domain registration checks using the IANA bootstrap registry."""

import json
import urllib.error
import urllib.request

BOOTSTRAP_URL = "https://data.iana.org/rdap/dns.json"
_SERVERS = None


def _request(url: str, timeout=8):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "BrandForge/1.0 (+https://github.com/star8592/BrandForge)"},
    )
    return urllib.request.urlopen(req, timeout=timeout)


def _load_servers():
    global _SERVERS
    if _SERVERS is not None:
        return _SERVERS

    with _request(BOOTSTRAP_URL) as response:
        payload = json.loads(response.read().decode("utf-8"))

    servers = {}
    for tlds, urls in payload.get("services", []):
        if not urls:
            continue
        for tld in tlds:
            servers[tld.lower()] = urls[0].rstrip("/") + "/"
    _SERVERS = servers
    return servers


def query(domain: str) -> dict:
    domain = domain.lower().strip(".")
    tld = domain.rsplit(".", 1)[-1]

    try:
        base = _load_servers().get(tld)
    except Exception as exc:
        return {"domain": domain, "status": "UNKNOWN", "error": f"bootstrap: {exc}"}

    if not base:
        return {"domain": domain, "status": "UNSUPPORTED"}

    url = base + "domain/" + domain
    try:
        with _request(url) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return {
            "domain": domain,
            "status": "REGISTERED",
            "rdap_name": payload.get("ldhName") or payload.get("unicodeName"),
        }
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {"domain": domain, "status": "AVAILABLE"}
        if exc.code in (400, 422):
            return {"domain": domain, "status": "INVALID_OR_UNSUPPORTED", "http": exc.code}
        return {"domain": domain, "status": "UNKNOWN", "http": exc.code}
    except Exception as exc:
        return {"domain": domain, "status": "UNKNOWN", "error": str(exc)}
