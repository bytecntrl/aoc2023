def solution(i: str) -> int:
    new_input = i.splitlines()
    result = [1] * len(new_input)

    for i, line in enumerate(new_input):
        correct, answer = [x.split() for x in line.split(": ")[-1].split(" | ")]
        correct_answer = set(correct) & set(answer)

        for j in range(i + 1, len(correct_answer) + i + 1):
            result[j] += result[i]

    return sum(result)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
