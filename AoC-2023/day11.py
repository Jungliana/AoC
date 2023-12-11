import numpy as np


def read_data(path: str) -> np.array:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append([1 if element == '#' else 0 for element in line.rstrip()])
    return np.array(lines)


def count_steps(data, multiplier: int) -> int:
    rows_empty = np.where(np.sum(data, axis=1) == 0)
    cols_empty = np.where(np.sum(data, axis=0) == 0)
    ys, xs = np.where(data == 1)
    steps = 0
    for i, i_val in enumerate(xs):
        for j in range(i+1, len(ys)):
            steps += abs(i_val - xs[j]) + abs(ys[i] - ys[j])
            if i_val > xs[j]:
                smaller = xs[j]
                bigger = i_val
            else:
                smaller = i_val
                bigger = xs[j]
            for element in cols_empty[0]:
                if smaller < element < bigger:
                    steps += multiplier
            if ys[i] > ys[j]:
                smaller = ys[j]
                bigger = ys[i]
            else:
                smaller = ys[i]
                bigger = ys[j]
            for element in rows_empty[0]:
                if smaller < element < bigger:
                    steps += multiplier
    return steps


def solve_part1(data: np.array) -> int:
    return count_steps(data, 1)


def solve_part2(data: np.array) -> int:
    return count_steps(data, 999999)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input11.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
