import argparse
from dataclasses import dataclass
import numpy as np


@dataclass
class Point:
    x: int
    y: int


def get_area(pt1: Point, pt2: Point):
    return (abs(pt1.x - pt2.x)+1) * (abs(pt1.y - pt2.y)+1)


def solve(data: list[Point]):
    current_area = get_area(data[0], data[1])
    for point1 in data:
        for point2 in data:
            current_area = max(current_area, get_area(point1, point2))

    return current_area


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.read().splitlines()
    data = []
    for idx, line in enumerate(content):
        x, y = line.split(",")
        data.append(Point(int(x), int(y)))
    res = solve(data)
    print(res)
