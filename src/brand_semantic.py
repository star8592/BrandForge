"""
Brand semantic evaluator.
Scores whether a generated name matches target company directions.
"""

DOMAINS = {
    "ai_infrastructure": ["ai", "agent", "intelligence", "core", "syn", "neuro"],
    "industrial": ["forge", "mach", "vector", "core", "engine"],
    "quant": ["quant", "alpha", "vector", "logic"],
    "education": ["learn", "mind", "academy", "knowledge"],
}


def semantic_score(name: str):
    text = name.lower()
    scores = {}
    for domain, words in DOMAINS.items():
        scores[domain] = sum(1 for w in words if w in text) * 10
    return scores


def evaluate(name: str):
    scores = semantic_score(name)
    return {
        "name": name,
        "scores": scores,
        "best_fit": max(scores, key=scores.get) if scores else None,
    }
