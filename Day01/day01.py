def load_data(path):
    with open(path) as file:
        data = file.read()
    return data.split("\n")


def sum_calories(data):
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
    return max(sum_calories(numbers))


def solve_part2(numbers):
    return sum(sorted(sum_calories(numbers), reverse=True)[0:3])


if __name__ == "__main__":
    numbers = load_data("Day01/input01.txt")
    print(f'Part 1 solution: {solve_part1(numbers)}')
    print(f'Part 2 solution: {solve_part2(numbers)}')
