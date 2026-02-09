import argparse
import numpy as np


def process_operation(numbers: list[int], operator: str) -> int:
    numbers = np.array(numbers, dtype=np.int64)
    if operator == "+":
        return np.sum(numbers)
    else:
        return np.prod(numbers)


def solve(data: list[str], operators: list[str]) -> int:
    total = 0
    operator_index = 0
    collected_columns = []
    for i in range(len(data[0])):
        column = [data[j][i] for j in range(len(data))]
        if all(c == "*" for c in column):
            total += process_operation(collected_columns,
                                       operators[operator_index])
            collected_columns = []
            operator_index += 1
        else:
            collected_columns.append(int("".join(column).replace("*", "")))
    total += process_operation(collected_columns,
                               operators[operator_index])
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.readlines()
        lines = content[:-1]
        operators = content[-1]

    for i, line in enumerate(lines):
        lines[i] = line.replace(" ", "*").replace("\n", "")
    operators = np.array([o for o in operators.split(" ") if o != ""])

    res = solve(lines, operators)
    print(res)
