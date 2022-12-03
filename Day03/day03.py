"""Day03 - puzzle solutions for day 03."""
import string
from difflib import SequenceMatcher
LETTER_LIST = list(string.ascii_letters)


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def find_double_points(backpack):
    """Find common item in two backpack's halves with SequenceMatcher."""
    backpack1 = backpack[:round(len(backpack)/2)]
    backpack2 = backpack[round(len(backpack)/2):len(backpack)]
    common = SequenceMatcher(None, backpack1, backpack2).find_longest_match()
    return LETTER_LIST.index(backpack[common.a])+1


def find_common_item(backpack):
    """Find common item in two backpack's halves."""
    backpack1 = backpack[:round(len(backpack)/2)]
    backpack2 = backpack[round(len(backpack)/2):len(backpack)]
    for item in backpack:
        if (item in backpack1) and (item in backpack2):
            return LETTER_LIST.index(item)+1
    return 0


def solve_part1(all_backpacks):
    """Solve part 1 of the puzzle."""
    points = 0
    for backpack in all_backpacks:
        points += find_common_item(backpack)
    return points


def find_badge(back1, back2, back3):
    """Find common item in 3 backpacks."""
    for item in back1:
        if (item in back2) and (item in back3):
            return LETTER_LIST.index(item)+1
    return 0


def solve_part2(all_backpacks):
    """Solve part 2 of the puzzle."""
    i = 0
    points = 0
    while i < len(all_backpacks):
        points += find_badge(all_backpacks[i], all_backpacks[i+1],
                             all_backpacks[i+2])
        i += 3
    return points


if __name__ == "__main__":
    data = load_data("Day03/input03.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    print(f'Part 2 answer: {solve_part2(data)}')
