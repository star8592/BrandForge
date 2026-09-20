from src.candidate_generator import generate
from src.scorer import score


def run():
    candidates = generate(200)
    results = []

    for name in candidates:
        results.append({
            "name": name,
            "score": score(name)
        })

    results.sort(key=lambda x: x['score'], reverse=True)

    for item in results[:20]:
        print(item)


if __name__ == '__main__':
    run()
