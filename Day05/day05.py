"""Day05 - puzzle solutions for day 05."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


if __name__ == "__main__":
    data = load_data("Day05/input05.txt")
    # print(f'Part 1 answer: {solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
