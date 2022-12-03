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
    backpack1 = backpack[:round(len(backpack)/2)]
    backpack2 = backpack[round(len(backpack)/2):len(backpack)]
    common = SequenceMatcher(None, backpack1, backpack2).find_longest_match()
    return LETTER_LIST.index(backpack[common.a])+1


def sum_points(all_backpacks):
    points = 0
    for backpack in all_backpacks:
        points += find_double_points(backpack)
    return points


if __name__ == "__main__":
    data = load_data("Day03/input03.txt")
    print(f'Part 1 answer: {sum_points(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
