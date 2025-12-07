import argparse
import numpy as np


def check_single(data: np.ndarray, coords: tuple[int, int]) -> bool:
    i, j = coords
    max_i = data.shape[0]
    max_j = data.shape[1]
    if i >= 0 and j >= 0 and i < max_i and j < max_j and data[i][j]:
        return True


def check_space(data: np.ndarray, i, j):
    if not data[i][j]:
        return 0, data
    to_check = [
        (i, j + 1),
        (i, j - 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i + 1, j + 1),
        (i - 1, j),
        (i - 1, j - 1),
        (i - 1, j + 1)]
    neighbours = []
    number = 0
    removed = 0
    for coords in to_check:
        if check_single(data, coords):
            number += 1
            neighbours.append(coords)

    if number < 4:
        removed += 1
        data[i][j] = False
        for n_i, n_j in neighbours:
            n_removed, data = check_space(data, n_i, n_j)
            removed += n_removed
    return removed, data


def solve(data: list[list[int]]) -> int:
    data = np.array(data)
    result = 0
    max_i = data.shape[0]
    max_j = data.shape[1]
    for i in range(max_i):
        for j in range(max_j):
            res, data = check_space(data, i, j)
            result += res
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        lines = f.read().splitlines()
    data = []
    for line in lines:
        data.append([i == "@" for i in line])
    res = solve(data)
    print(res)
