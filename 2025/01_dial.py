import argparse


def trim(current: int) -> int:
    if current < 0:
        current += 100
    if current > 99:
        current -= 100
    return current


def shift(current: int, value: int, symbol: str) -> int:
    if symbol == "L":
        current -= value
    if symbol == "R":
        current += value
    return current


def solve(data: list[str]) -> int:
    current = 50
    result = 0
    for line in data:
        symbol = line[0]
        value = int(line[1:])
        if value > 99:
            result += value // 100
            value %= 100
        shifted = shift(current, value, symbol)
        trimmed = trim(shifted)
        if current != 0 and (trimmed != shifted or trimmed == 0):
            result += 1
        current = trimmed
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        data = f.read().splitlines()
    res = solve(data)
    print(res)
