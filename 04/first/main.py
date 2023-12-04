def solution(i: str) -> int:
    result: int = 0

    for line in i.splitlines():
        correct, answer = [x.split() for x in line.split(": ")[-1].split(" | ")]
        correct_answer = set(correct) & set(answer)
        result += 2 ** (len(correct_answer) - 1) if len(correct_answer) > 0 else 0

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
