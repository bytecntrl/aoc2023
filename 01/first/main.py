def solution(i: str) -> int:
    result: int = 0

    for line in i.splitlines():
        first, *last = [y for y in line if y.isdigit()]
        result += int(first + (first if len(last) == 0 else last[-1]))

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
