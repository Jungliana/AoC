"""Day04 - puzzle solutions for day 04."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip().split(','))
    return lines


def get_ints(ranges):
    """Change ranges in string to ints."""
    x = ranges[0].split('-')
    y = ranges[1].split('-')
    return (int(x[0]), int(x[1]), int(y[0]), int(y[1]))


def check_range_in_other(ranges) -> bool:
    if ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
        return True
    return (ranges[2] >= ranges[0] and ranges[3] <= ranges[1])


def solve_part1(range_list):
    fully_contains = 0
    for assignment in range_list:
        fully_contains += 1 if check_range_in_other(get_ints(assignment)) else 0
    return fully_contains


if __name__ == "__main__":
    data = load_data("Day04/input04.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
