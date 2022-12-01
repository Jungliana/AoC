"""Day01 - puzzle solutions for day 01."""


def load_data(path):
    """Load and split data from file."""
    with open(path, encoding=ascii) as file:
        data = file.read()
    return data.split("\n")


def sum_calories(data):
    """Sum calories for every elf."""
    calories = 0
    elf_calories = []

    for number in data:
        if number:
            calories += int(number)
        else:
            elf_calories.append(calories)
            calories = 0
    return elf_calories


def solve_part1(numbers):
    """Solve part 1 of the puzzle."""
    return max(sum_calories(numbers))


def solve_part2(numbers):
    """Solve part 2 of the puzzle."""
    return sum(sorted(sum_calories(numbers), reverse=True)[0:3])


if __name__ == "__main__":
    number_list = load_data("Day01/input01.txt")
    print(f'Part 1 solution: {solve_part1(number_list)}')
    print(f'Part 2 solution: {solve_part2(number_list)}')
