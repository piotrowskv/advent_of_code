import argparse


def generate_possible_ranges(ranges: list[tuple[int, int]]):
    total_range = []
    for r in ranges:
        if len(total_range) == 0:
            total_range.append(r)
            continue
        begin, end = r
        last_begin, last_end = total_range[-1]
        if begin > last_end:
            total_range.append(r)
            continue
        if end > last_end:
            total_range[-1] = (last_begin, end)
    return total_range


def solve(ranges: list[str], ids: list[str]) -> int:
    del ids
    result = 0
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]
    ranges.sort(key=lambda x: x[0])
    total_range = generate_possible_ranges(ranges)
    for r in total_range:
        begin, end = r
        result += (end - begin + 1)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        data = f.read().splitlines()
    breakline = data.index("")
    ranges = data[:breakline]
    ids = data[breakline+1:]
    res = solve(ranges, ids)
    print(res)
