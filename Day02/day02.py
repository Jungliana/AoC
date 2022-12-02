"""Day02 - puzzle solutions for day 02."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


# A, X - rock (1); B, Y - paper (2); C, Z - scissors (3)
# 0 - loss, 3 - draw, 6 - win
def point_dict(play_round):
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


def solve_part1(letters):
    result = 0
    for line in letters:
        result += point_dict(line) 
    return result


def solve_part2(letters):
    pass


if __name__ == "__main__":
    data = load_data("Day02/input02.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
