"""Deterministic brand scoring for the BrandForge MVP."""

import re

AI_ROOTS = {"syn": 10, "cogn": 9, "neuro": 8, "axi": 7, "nex": 6, "core": 5}
INDUSTRIAL_ROOTS = {"forge": 10, "vector": 9, "core": 8, "terra": 5}
QUANT_ROOTS = {"quant": 10, "vector": 8, "axi": 5, "pulse": 4}
GOOD_SUFFIXES = {"ora": 10, "ara": 8, "ia": 7, "ix": 5, "on": 5, "os": 4, "um": 3}

KNOWN_COLLISIONS = {
    "axios", "lumia", "lumix", "nexon", "cognos", "axion",
    "oracle", "meta", "apple", "amazon", "tesla", "openai",
}


def _root_score(name: str, mapping: dict[str, int]) -> int:
    return max((value for root, value in mapping.items() if root in name), default=0)


def brandability(name: str) -> float:
    n = name.lower()
    score = 30.0
    length = len(n)
    if length < 5:
        score -= (5 - length) * 4
    elif length > 9:
        score -= (length - 9) * 3
    vowels = sum(ch in "aeiouy" for ch in n)
    ratio = vowels / max(length, 1)
    if ratio < 0.25 or ratio > 0.62:
        score -= 5

    if re.search(r"[aeiou]{3,}|[^aeiou]{4,}", n):
        score -= 7
    if re.search(r"(.)\1", n):
        score -= 5
    if any(x in n for x in ("oraora", "araara", "iia", "oora", "aara")):
        score -= 8

    suffix_bonus = max((v for s, v in GOOD_SUFFIXES.items() if n.endswith(s)), default=0)
    score += suffix_bonus * 0.4
    return max(0.0, min(34.0, score))


def evaluate_brand(name: str) -> dict:
    n = name.lower()
    brand = brandability(n)
    ai = _root_score(n, AI_ROOTS) * 2.0
    industrial = _root_score(n, INDUSTRIAL_ROOTS) * 1.4
    quant = _root_score(n, QUANT_ROOTS) * 1.2
    collision_penalty = 22.0 if n in KNOWN_COLLISIONS else 0.0

    # Prefer names that can stretch across several of the user's product lines.
    breadth = sum(component > 0 for component in (ai, industrial, quant))
    breadth_bonus = max(0, breadth - 1) * 3.0

    raw = brand + ai + industrial + quant + breadth_bonus - collision_penalty
    overall = round(max(0.0, min(100.0, raw)), 2)

    return {
        "name": n,
        "score": overall,
        "brandability": round(brand, 2),
        "ai_fit": round(ai, 2),
        "industrial_fit": round(industrial, 2),
        "quant_fit": round(quant, 2),
        "breadth_bonus": round(breadth_bonus, 2),
        "collision_penalty": round(collision_penalty, 2),
    }


def score_candidate(candidate: str) -> float:
    return evaluate_brand(candidate)["score"]


def score(candidate: str, signals=None) -> float:
    """Backward-compatible entry point."""
    if signals:
        return round(
            signals.get("domain", 0) * 0.25
            + signals.get("uniqueness", 0) * 0.25
            + signals.get("future_fit", 0) * 0.30
            + signals.get("conflict", 0) * 0.20,
            2,
        )
    return score_candidate(candidate)
