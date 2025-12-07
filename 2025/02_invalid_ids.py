import argparse


def check_range(value: str, chunk_size: int) -> bool:
    base = value[0:chunk_size]
    for j in range(len(value), 2*chunk_size - 1, -chunk_size):
        token = value[j-chunk_size:j]
        if token != base:
            return False
    return True


def is_invalid(value: str) -> bool:
    for i in range(len(value) // 2, 0, -1):
        if len(value) % i != 0:
            continue
        if check_range(value, i):
            return True
    return False


def solve(data: list[str]) -> int:
    result = 0
    for line in data:
        begin, end = line.split("-")
        for number in range(int(begin), int(end) + 1):
            string = str(number)
            if is_invalid(string):
                result += number

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        data = f.read().split(",")
    res = solve(data)
    print(res)
