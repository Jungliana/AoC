def read_data(path: str) -> list[list[str]]:
    with open(path, encoding="ASCII") as file:
        file_lines = file.readlines()

    seeds = ([int(seed) for seed in file_lines[0].lstrip('seeds: ').rstrip('\n').split()])
    all_maps = []

    line_id = 2
    for _ in range(7):
        map_type = file_lines[line_id].rstrip(' map:\n').split('-to-')
        line_id += 1
        ranges = []
        while file_lines[line_id] != '\n':
            ranges.append([int(value) for value in file_lines[line_id].rstrip().split()])
            line_id += 1
        all_maps.append(Map(map_type[0], map_type[1], ranges))
        line_id += 1

    return seeds, all_maps


class Map:
    def __init__(self, map_from, map_to, ranges) -> None:
        self.map_from = map_from
        self.map_to = map_to
        self.ranges = ranges

    def __str__(self) -> str:
        return f'Map from {self.map_from} to {self.map_to}'

    def map_value(self, value: int) -> int:
        for rangee in self.ranges:
            if rangee[1] <= value < rangee[1]+rangee[2]:
                return rangee[0] + (value - rangee[1])
        return value

    def map_backwards(self, value: int) -> int:
        for rangee in self.ranges:
            if rangee[0] <= value < rangee[0]+rangee[2]:
                return rangee[1] + (value - rangee[0])
        return value


def solve_part1(seeds, data) -> int:
    for map_obj in data:
        seeds = [map_obj.map_value(seed) for seed in seeds]
    return min(seeds)


def solve_part2(seeds, data) -> int:
    seed_set = set()

    for i in range(0, len(seeds)-1, 2):
        seed_set.update(range(seeds[i], seeds[i]+seeds[i+1]))

    reversed_maps = list(reversed(data))
    location = -1
    seed = 0
    while seed not in seed_set:
        location += 1
        seed = location
        for map_obj in reversed_maps:
            seed = map_obj.map_backwards(seed)
    return location


if __name__ == "__main__":
    data_seeds, data_input = read_data("AoC-2023/inputs/input05.txt")
    print(f'Part 1 solution: {solve_part1(data_seeds, data_input)}')
    # print(f'Part 2 solution: {solve_part2(data_seeds, data_input)}')
