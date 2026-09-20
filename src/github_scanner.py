"""
BrandForge GitHub collision scanner.
"""

import urllib.request


NAMES = []


def check_github(name: str):
    candidates = [
        name,
        f"{name}-ai",
        f"{name}-labs",
    ]

    output = []

    for item in candidates:
        url = f"https://github.com/{item}"
        try:
            with urllib.request.urlopen(url, timeout=5) as r:
                output.append({"name": item, "used": r.status == 200})
        except Exception:
            output.append({"name": item, "used": False})

    return output


if __name__ == "__main__":
    print(check_github("synora"))
