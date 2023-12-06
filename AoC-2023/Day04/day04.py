from collections import defaultdict


def read_data(path: str) -> list[list[str]]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(line.rstrip().split(":"))
    return lines


def count_winning(line):
    all_nums = line.split(" | ")
    winning = set()
    winning.update([int(number) for number in all_nums[0].split()])

    have = set()
    have.update([int(number) for number in all_nums[1].split()])

    have_winning = len(winning.intersection(have))
    return have_winning


def solve_part1(data):
    points = 0
    for line in data:
        if (point_power := count_winning(line[1])-1) >= 0:
            points += 2 ** point_power
    return points


def solve_part2(data):
    all_copies = defaultdict(int)
    for line in data:
        card_id = int(line[0].split()[1])
        all_copies[card_id] += 1

        copies = count_winning(line[1])
        for i in range(card_id+1, card_id+copies+1):
            all_copies[i] += all_copies[card_id]

    return sum(all_copies.values())


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input04.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
