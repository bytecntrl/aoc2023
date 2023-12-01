LETTER_TO_NUMBER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(i: str) -> int:
    result: int = 0
    new_input = []

    for line in i.splitlines():
        tmp = []

        for ind in range(len(line)):
            for k, v in LETTER_TO_NUMBER.items():
                if line[ind:].startswith(k):
                    tmp.append(v)
            else:
                tmp.append(line[ind])

        new_input.append("".join(tmp))

    for line in new_input:
        first, *last = [y for y in line if y.isdigit()]
        result += int(first + (first if len(last) == 0 else last[-1]))

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read()))
