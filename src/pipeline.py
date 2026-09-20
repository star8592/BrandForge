"""
BrandForge v0.5 pipeline.
Combines generation, scoring and semantic analysis.
"""

from src.brand_semantic import evaluate


def run_pipeline(names):
    results = []
    for name in names:
        results.append(evaluate(name))
    return sorted(
        results,
        key=lambda x: max(x["scores"].values()) if x["scores"] else 0,
        reverse=True,
    )
