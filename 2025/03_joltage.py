import argparse


def max_index(value: str) -> tuple[int, int]:
    max_ = max(value)
    max_index = value.index(max_)
    return int(max_), max_index


def parse_number(digits: list[int]) -> int:
    number = 0
    for digit in digits:
        number *= 10
        number += digit
    return number


def solve(data: list[str]) -> int:
    result = 0
    for line in data:
        digits = []
        index = -1
        for i in range(11, -1, -1):
            avaliable = line[index+1: len(line)-i]
            digit, offset = max_index(avaliable)
            index += offset + 1
            digits.append(digit)
        result += parse_number(digits)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        data = f.read().splitlines()
    res = solve(data)
    print(res)
