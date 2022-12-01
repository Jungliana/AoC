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


if __name__ == "__main__":
    numbers = load_data("Day01/input01.txt")
    print(max(sum_calories(numbers)))
    calories_list = sum_calories(numbers)
    print(sum(sorted(calories_list, reverse=True)[0:3]))
