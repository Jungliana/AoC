"""Day04 - puzzle solutions for day 04."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip().split(','))
    return lines


def get_ints(ranges: list[str]) -> tuple[int]:
    """Change ranges in string to ints."""
    r_1 = ranges[0].split('-')
    r_2 = ranges[1].split('-')
    return (int(r_1[0]), int(r_1[1]), int(r_2[0]), int(r_2[1]))


def range_in_other(ranges: tuple[int]) -> bool:
    """Check if one of the ranges contains the other."""
    if ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
        return True
    return (ranges[2] >= ranges[0] and ranges[3] <= ranges[1])


def solve_part1(range_list: list[list[str]]) -> int:
    """Solve part 1 of the puzzle."""
    fully_contains = 0
    for assignment in range_list:
        fully_contains += 1 if range_in_other(get_ints(assignment)) else 0
    return fully_contains


def ranges_overlap(ranges: tuple[int]) -> bool:
    """Check if two ranges overlap."""
    first = range(ranges[0], ranges[1]+1)
    second = range(ranges[2], ranges[3]+1)
    for number in first:
        if number in second:
            return True
    return False


def solve_part2(range_list: list[list[str]]) -> int:
    """Solve part 2 of the puzzle."""
    fully_contains = 0
    for assignment in range_list:
        fully_contains += 1 if ranges_overlap(get_ints(assignment)) else 0
    return fully_contains


if __name__ == "__main__":
    data = load_data("Day04/input04.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    print(f'Part 2 answer: {solve_part2(data)}')
