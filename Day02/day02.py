"""Day02 - puzzle solutions for day 02."""
from collections.abc import Callable


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


# A, X - rock (1); B, Y - paper (2); C, Z - scissors (3)
# 0 - loss, 3 - draw, 6 - win
def point_dict_1(play_round: str) -> int:
    """Read round result from dictionary."""
    points = {'A X': 4,
              'B X': 1,
              'C X': 7,
              'A Y': 8,
              'B Y': 5,
              'C Y': 2,
              'A Z': 3,
              'B Z': 9,
              'C Z': 6}
    return points[play_round]


def solve(letters: list[str], chosen_dict: Callable[[list[str]], int]) -> int:
    """Count points using chosen dictionary."""
    result = 0
    for line in letters:
        result += chosen_dict(line)
    return result


# A - rock (1); B - paper (2); C - scissors (3)
# X - loss (0), Y - draw (3), Z - win (6)
def point_dict_2(play_round: str) -> int:
    """Read round result from dictionary."""
    points = {'A X': 3,
              'B X': 1,
              'C X': 2,
              'A Y': 4,
              'B Y': 5,
              'C Y': 6,
              'A Z': 8,
              'B Z': 9,
              'C Z': 7}
    return points[play_round]


def solve_part1(letters: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return solve(letters, point_dict_1)


def solve_part2(letters: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return solve(letters, point_dict_2)


if __name__ == "__main__":
    data = load_data("Day02/input02.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    print(f'Part 2 answer: {solve_part2(data)}')
