def score(candidate, signals):
    """Simple extensible brand score.

    signals:
    - domain
    - uniqueness
    - future_fit
    - conflict
    """
    return (
        signals.get("domain", 0) * 0.25
        + signals.get("uniqueness", 0) * 0.25
        + signals.get("future_fit", 0) * 0.30
        + signals.get("conflict", 0) * 0.20
    )
