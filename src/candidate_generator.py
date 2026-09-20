"""
BrandForge candidate generator
Generate technology brand candidates from phonetic roots.
"""

ROOTS = [
    "nex", "syn", "axi", "lum", "nova", "velo",
    "cogn", "neuro", "forge", "vector", "quant",
    "core", "terra", "pulse"
]

SUFFIXES = [
    "ora", "ara", "ia", "ix", "on", "os", "um"
]


def generate(limit=1000):
    result = []
    seen = set()

    for root in ROOTS:
        for suffix in SUFFIXES:
            name = (root + suffix).lower()
            if name not in seen:
                seen.add(name)
                result.append(name)

    return result[:limit]


if __name__ == "__main__":
    for item in generate():
        print(item)
