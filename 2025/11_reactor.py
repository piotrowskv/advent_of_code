
import argparse


def solve(data: dict[str, list[str]]):

    data['out'] = []

    def get_number_of_paths(start: str, end: str):
        path_len = {node: 0 for node in data}
        path_len[end] = 1
        changed = True
        while changed:
            prev_paths = {**path_len}
            path_len = {
                node: 1 if node == end else sum(
                    prev_paths[child] for child in data[node]
                )
                for node in prev_paths
            }
            if prev_paths == path_len:
                changed = False
        return path_len[start]

    fft_to_dac = 1
    for start, end in [('svr', 'fft'), ('fft', 'dac'), ('dac', 'out')]:
        fft_to_dac *= get_number_of_paths(start, end)

    dac_to_fft = 1
    for start, end in [('svr', 'dac'), ('dac', 'fft'), ('fft', 'out')]:
        dac_to_fft *= get_number_of_paths(start, end)

    return fft_to_dac + dac_to_fft


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', metavar='path', required=True)
    args = parser.parse_args()
    with open(args.file, "r+", encoding="UTF-8") as f:
        content = f.read().splitlines()
    data = {}
    for line in content:
        node = line.split(":")[0]
        children = [c for c in line.split(":")[1].split(" ") if c != ""]
        data[node] = children
    res = solve(data)
    print(res)
