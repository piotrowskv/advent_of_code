import argparse
import numpy as np
from functools import lru_cache


def solve(data: np.ndarray) -> int:

    @lru_cache
    def downward(x, y) -> int:
        max_x, _ = data.shape
        if x > max_x:
            return 1
        match data[x+1][y]:
            case ".":
                return downward(x+1, y)
            case "^":
                return downward(x, y - 1) + downward(x, y + 1)

    init_y = np.argwhere(data[0] == "S")[0][0]
    return downward(0, init_y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.read().splitlines()
    for i, line in enumerate(content):
        content[i] = [char for char in line]
    content = np.array(content)
    res = solve(content)
    print(res)
