"""Generate a compact, pronounceable technology-brand candidate pool."""

import re

ROOTS = [
    "nex", "syn", "axi", "lum", "cogn", "aev", "orb", "zen",
    "tens", "flux", "kin", "arv", "vey", "ely", "orv", "zyn",
]

SUFFIXES = ["ora", "ara", "ia", "ix", "on", "os", "um", "eva", "ero"]

CURATED = [
    "nexara", "synora", "axiora", "arvora", "veyora", "orvexa",
    "elyora", "novyra", "zynera", "aevora", "corevia", "forgevia",
    "quantivo", "cogniva", "neurava", "vectara", "tensora", "fluxora",
    "kinora", "orvian", "aevian", "velyra", "synera", "nexivo",
    "axivra", "coryva", "zenora", "elyvia", "arvexa", "veyron",
]

BLOCKED = {
    "axios", "lumia", "lumix", "nexon", "cognos", "axion",
    "oracle", "meta", "apple", "amazon", "tesla", "openai",
}


def plausible(name: str) -> bool:
    n = name.lower()
    if n in BLOCKED or not (5 <= len(n) <= 9):
        return False
    if re.search(r"[aeiou]{3,}|[^aeiou]{5,}", n):
        return False
    if any(bad in n for bad in ("oora", "aara", "iia", "aa", "uu", "ii")):
        return False
    return True


def generate(limit=1000):
    result = []
    seen = set()

    for name in CURATED:
        if plausible(name) and name not in seen:
            seen.add(name)
            result.append(name)

    for root in ROOTS:
        for suffix in SUFFIXES:
            name = (root + suffix).lower()
            if plausible(name) and name not in seen:
                seen.add(name)
                result.append(name)

    return result[:limit]


if __name__ == "__main__":
    for item in generate():
        print(item)
