import regex as re


INTEGERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

REGEX = "zero|one|two|three|four|five|six|seven|eight|nine"


def read_data(path: str) -> list[str]:
    with open(path, encoding="ASCII") as file:
        lines = file.readlines()
    return lines


def find_integers(data: list[str]) -> list[list[int]]:
    return [list(map(int, filter(str.isdigit, [*line]))) for line in data]


def find_word_integers(data: list[str]) -> list[list[int]]:
    return [list(map(lambda x: INTEGERS[x], re.findall(REGEX, line))) for line in data]


def insert_integers_from_words(data: list[str]) -> list[str]:
    added_nums = []
    for line in data:
        result = re.finditer(REGEX, line, overlapped=True)
        newline = line
        for i, match_obj in enumerate(result):
            start = match_obj.start(0)
            value = match_obj.group(0)
            newline = newline[:start+i] + INTEGERS[value] + newline[start+i:]
        added_nums.append(newline)
    return added_nums


def sum_integers(data: list[list[int]]) -> int:
    return sum(10 * line[0] + line[-1] for line in data if line)


def solve_part1(data: list[str]) -> int:
    return sum_integers(find_integers(data))


def solve_part2(data: list[str]) -> int:
    data = insert_integers_from_words(data)
    data = find_integers(data)
    return sum_integers(data)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input01.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
