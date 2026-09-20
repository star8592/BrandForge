"""BrandForge v1.0 MVP pipeline entry.

This module intentionally keeps the pipeline small:
1. generate candidates
2. score candidates
3. prepare ranking output

External checks can be plugged in later without changing the core flow.
"""

from pathlib import Path
import json

from candidate_generator import generate_candidates
from scorer import score_candidate


OUTPUT = Path("reports")


def run(limit=100):
    OUTPUT.mkdir(exist_ok=True)
    candidates = generate_candidates()
    ranked = []

    for name in candidates[:limit]:
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
    print(run())
