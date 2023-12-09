def read_data(path: str) -> list[list[str]]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append([int(element) for element in line.rstrip().split()])
    return lines


def extrapolate(series: list[int], backward: bool = False) -> int:
    if all(element == 0 for element in series):
        return 0
    new_series = [original - shifted for original,
                  shifted in zip(series[1:], series[:-1])]
    if backward:
        return series[0] - extrapolate(new_series, backward=True)
    return extrapolate(new_series) + series[-1]


def solve_part1(data: list[list[int]]) -> int:
    counter = 0
    for line in data:
        counter += extrapolate(line)
    return counter


def solve_part2(data: list[list[int]]) -> int:
    counter = 0
    for line in data:
        counter += extrapolate(line, backward=True)
    return counter


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input09.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
