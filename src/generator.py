from pathlib import Path

SUFFIXES = [
    "ora",
    "ara",
    "ia",
    "ix",
    "os",
    "um",
]


def generate(seeds):
    result = set()
    for seed in seeds:
        for suffix in SUFFIXES:
            result.add(seed + suffix)
    return sorted(result)


if __name__ == "__main__":
    seeds = [
        x.strip()
        for x in Path("data/seeds.txt").read_text().splitlines()
        if x.strip()
    ]

    for item in generate(seeds):
        print(item)
