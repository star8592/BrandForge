"""BrandForge v1.0 MVP pipeline entry.

Minimal runnable pipeline:
1. generate candidates
2. score candidates
3. export ranking output
"""

from pathlib import Path
import json

from candidate_generator import generate
from scorer import score_candidate


OUTPUT = Path("reports")


def run(limit=1000):
    OUTPUT.mkdir(exist_ok=True)

    candidates = generate(limit=limit)
    ranked = []

    for name in candidates:
        ranked.append({
            "name": name,
            "score": score_candidate(name)
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)

    result = OUTPUT / "top_brands.json"
    result.write_text(
        json.dumps(ranked[:50], indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return ranked[:50]


if __name__ == "__main__":
    for item in run():
        print(item)
