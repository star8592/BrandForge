"""Brand search pollution risk scoring foundation."""


def score_search_risk(results: int, has_company: bool = False):
    score = 0
    if results > 100000:
        score += 60
    elif results > 10000:
        score += 40
    elif results > 1000:
        score += 20

    if has_company:
        score += 30

    return min(score, 100)


def classify(score: int):
    if score < 30:
        return "LOW"
    if score < 70:
        return "MEDIUM"
    return "HIGH"
