"""Day01 - puzzle solutions for day 01."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    with open(path, encoding="ascii") as file:
        lines = file.read()
    return lines.split("\n")


def sum_calories(lines: list[str]) -> list[int]:
    """Sum calories for every elf."""
    calories = 0
    elf_calories = []

    for number in lines:
        if number:
            calories += int(number)
        else:
            elf_calories.append(calories)
            calories = 0
    return elf_calories


def solve_part1(numbers: list[int]) -> int:
    """Solve part 1 of the puzzle."""
    return max(sum_calories(numbers))


def solve_part2(numbers: list[int]) -> int:
    """Solve part 2 of the puzzle."""
    return sum(sorted(sum_calories(numbers), reverse=True)[0:3])


if __name__ == "__main__":
    data = load_data("Day01/input01.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    print(f'Part 2 answer: {solve_part2(data)}')
