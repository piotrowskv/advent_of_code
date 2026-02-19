from math import sqrt
import argparse
import numpy as np

type Point = tuple[int, int, int]


def distance(pt1: Point, pt2: Point):
    return sqrt(
        (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 + (pt1[2] - pt2[2]) ** 2)


def solve(data: list[Point]):
    distances = {}
    for i_idx, i in enumerate(data):
        for j_idx, j in enumerate(data[:i_idx]):
            if i_idx == j_idx:
                continue
            distances[(i_idx, j_idx)] = distance(i, j)
    results: dict[int, int] = {i: -1 for i in range(len(data))}
    connected: set[int] = set()
    sets: list[set[int]] = []

    while len(connected) < len(data):
        print(len(data) - len(connected))
        min_val = min(distances.values())
        min_i, min_j = next(k for k, v in distances.items() if v == min_val)
        del distances[(min_i, min_j)]
        connected.add(min_i)
        connected.add(min_j)

        if results[min_i] == results[min_j] and results[min_i] > -1:
            continue
        if results[min_i] == results[min_j] == -1:
            sets.append({min_i, min_j})
            results[min_i] = len(sets) - 1
            results[min_j] = len(sets)-1
        elif results[min_j] == -1:
            results[min_j] = results[min_i]
            sets[results[min_i]].add(min_j)
        elif results[min_i] == -1:
            results[min_i] = results[min_j]
            sets[results[min_j]].add(min_i)
        else:
            set_i = sets[results[min_i]]
            set_j = sets[results[min_j]]
            sets[results[min_i]] = set()
            sets[results[min_j]] = set()
            new_set = set_i.union(set_j)
            sets.append(new_set)
            for val in new_set:
                results[val] = len(sets)-1

    return data[min_i][0]*data[min_j][0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.read().splitlines()
    data = []
    for idx, line in enumerate(content):
        x, y, z = line.split(",")
        data.append((int(x), int(y), int(z)))
    res = solve(data)
    print(res)
