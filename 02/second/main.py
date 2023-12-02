import collections
import functools


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

    return sum([functools.reduce(lambda x, y: x * y, x.values()) for x in new_input])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
