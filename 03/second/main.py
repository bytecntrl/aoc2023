import collections
import re


def get_adjacent_position(n: int, x: int, y: int) -> list[tuple[int, int]]:
    p = []

    for i in range(n):
        p.append((x + 1, y + i))
        p.append((x - 1, y + i))

    p.append((x, y - 1))
    p.append((x, y + n))
    p.append((x - 1, y - 1))
    p.append((x - 1, y + n))
    p.append((x + 1, y - 1))
    p.append((x + 1, y + n))

    return [x for x in p if x[0] >= 0 and x[1] >= 0]


def solution(i: str) -> int:
    new_input = []
    number_position = []
    special_char_position = []
    result = collections.defaultdict(lambda: [0, 1])

    for line in i.splitlines():
        tmp = []
        position = []
        row = [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", line) if x]

        for x in row:
            if isinstance(x, str):
                tmp.extend(list(x))
            else:
                tmp.append(x)

        for i, x in enumerate(tmp):
            position.append(
                (
                    x,
                    len(str(x)) if isinstance(x, int) else 1,
                    0 if i == 0 else (position[-1][1] + position[-1][2]),
                )
            )

        new_input.append(position)

    for i, x in enumerate(new_input):
        for n, c, p in x:
            if isinstance(n, int):
                number_position.append((n, c, i, p))
            elif n == "*":
                special_char_position.append((i, p))

    for n, c, x, y in number_position:
        for z in get_adjacent_position(c, x, y):
            if z in special_char_position:
                result[z][0] += 1
                result[z][1] *= n
                break

    return sum([v for n, v in result.values() if n >= 2])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
