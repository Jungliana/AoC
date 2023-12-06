from numpy import roots, ceil, floor


def read_data(path: str) -> list[list[str]]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(line.rstrip().split(":")[1])
    return lines


def ways_to_win(time, distance):
    coeff = [-1, time, -distance]
    xs = roots(coeff)
    xs.sort()
    return int((ceil(xs[1]) - floor(xs[0])) - 1)


def solve_part1(data):
    times = [int(number) for number in data[0].split()]
    distances = [int(number) for number in data[1].split()]
    ways_multiplied = 1
    for time, distance in zip(times, distances):
        ways_multiplied *= ways_to_win(time, distance)
    return ways_multiplied


def solve_part2(data):
    time = int("".join(data[0].split()))
    distance = int("".join(data[1].split()))
    return ways_to_win(time, distance)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input06.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
