"""Day02 - puzzle solutions for day 02."""

# A, X - rock (1); B, Y - paper (2); C, Z - scissors (3)
# 0 - loss, 3 - draw, 6 - win
POINTS1 = {'A X': 4, 'B X': 1, 'C X': 7,
           'A Y': 8, 'B Y': 5, 'C Y': 2,
           'A Z': 3, 'B Z': 9, 'C Z': 6}

# A - rock (1); B - paper (2); C - scissors (3)
# X - loss (0), Y - draw (3), Z - win (6)
POINTS2 = {'A X': 3, 'B X': 1, 'C X': 2,
           'A Y': 4, 'B Y': 5, 'C Y': 6,
           'A Z': 8, 'B Z': 9, 'C Z': 7}


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def solve(letters: list[str], chosen_dict: dict) -> int:
    """Count points using chosen dictionary."""
    result = 0
    for line in letters:
        result += chosen_dict[line]
    return result


def solve_part1(letters: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return solve(letters, POINTS1)


def solve_part2(letters: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return solve(letters, POINTS2)


if __name__ == "__main__":
    data = load_data("Day02/input02.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    print(f'Part 2 answer: {solve_part2(data)}')
