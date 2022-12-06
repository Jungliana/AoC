"""Day06 - puzzle solutions for day 06."""


def load_data(path: str) -> str:
    """Load and split data from file."""
    with open(path, encoding="ascii") as file:
        return file.readlines()[0]


if __name__ == "__main__":
    data = load_data("Day06/input06.txt")
    # print(f'Part 1 answer: {solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
