
import argparse
import re
import itertools
import numpy as np
from scipy.optimize import linprog


def solve_single(data: tuple[list[int], np.ndarray]):
    pattern, buttons = data
    x = linprog(pattern, A_eq=buttons, b_eq=np.zeros(
        (1, buttons.shape[0])), bounds=(0, None))
    print(x)
    return np.sum(x.x)


def solve(data: list[tuple[int, list[list[int]]]]):
    sum = 0
    for d in data:
        sum += solve_single(d)
    return sum


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.read().splitlines()
    data = []
    for line in content:
        match = re.search(
            r"(\[[.#]+\]) ((?:(\([0-9,]+\))\s)+)(\{[0-9,]+\})", line)
        pattern = [int(b) for b in (match.group(4)[1:-1].split(","))]

        digits = [b for b in match.group(2).split(" ") if b != ""]
        buttons = np.zeros((len(digits), len(pattern)))
        for idx, button_digits in enumerate(digits):
            for b in button_digits[1:-1].split(","):
                if b in ["", " ", "\n"]:
                    continue
                buttons[idx][int(b)] = 1
        data.append((pattern, buttons))
    res = solve(data)
    print(res)
