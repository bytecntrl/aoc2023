import collections


COLOR_MAX = {"red": 12, "green": 13, "blue": 14}


def solution(i: str) -> int:
    new_input = []

    for line in i.splitlines():
        tmp = collections.defaultdict(int)
        line = line.split(": ")[-1]

        for game in line.split("; "):
            game_totals = collections.defaultdict(int)

            for c in game.split(", "):
                n, color = c.split(" ")
                game_totals[color] += int(n)

            for k, v in game_totals.items():
                tmp[k] = max(tmp[k], v)

        new_input.append(dict(tmp))

    return sum(
        [
            (i + 1)
            for i, x in enumerate(new_input)
            if all([COLOR_MAX[k] >= v for k, v in x.items()])
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
