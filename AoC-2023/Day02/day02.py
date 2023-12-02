class Game:
    def __init__(self, game_id: int) -> None:
        self.id: int = game_id
        self.cubes = {"red": [], "green": [], "blue": []}

    def id_game_possible(self, all_cubes: list[tuple]) -> int:
        for cube_set in all_cubes:
            if max(self.cubes[cube_set[0]]) > cube_set[1]:
                return 0
        return self.id

    def power_of_set(self) -> int:
        power = 1
        for cube_values in self.cubes.values():
            power *= max(cube_values)
        return power


def read_data(path: str) -> list[Game]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(process_line_of_data(line))
    return lines


def process_line_of_data(line: str) -> Game:
    games = line.rstrip("\n").split(":")
    game_id = int(games[0].split()[1])
    game_obj = Game(game_id)
    examples_split = games[1].split(";")
    for example in examples_split:
        cubes_split = example.split(",")
        for element in cubes_split:
            element = element.split()
            game_obj.cubes[element[1]].append(int(element[0]))
    return game_obj


def solve_part1(data, tuples):
    return sum(game.id_game_possible(tuples) for game in data)


def solve_part2(data):
    return sum(game.power_of_set() for game in data)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/Day02/input02.txt")
    color_nums = [("red", 12), ("green", 13), ("blue", 14)]
    print(f'Part 1 solution: {solve_part1(data_input, color_nums)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
