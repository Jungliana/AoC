class Game:
    def __init__(self, game_id: int) -> None:
        self.id = game_id
        self.cubes = {"red": [], "green": [], "blue": []}

    def __str__(self) -> str:
        return f'Game: {self.id}'

    def id_game_possible(self, all_cubes: list[tuple]) -> int:
        for cube_set in all_cubes:
            if max(self.cubes[cube_set[0]]) > cube_set[1]:
                return 0
        return self.id

    def set_power(self) -> int:
        power = 1
        for cube_values in self.cubes.values():
            power *= max(cube_values)
        return power


def read_data(path: str) -> list[str]:
    with open(path, encoding="ASCII") as file:
        lines = file.readlines()
    return lines


def process_line_of_data(line: str) -> Game:
    # Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green; 11 green, 6 blue; 8 blue, 12 green
    games = line.rstrip("\n").split(":")
    game_id = int(games[0].split()[1])
    game_obj = Game(game_id)
    games_splitted = games[1].split(";")
    for game in games_splitted:
        cubes_split = game.split(",")
        for element in cubes_split:
            element = element.split()
            game_obj.cubes[element[1]].append(int(element[0]))
    return game_obj


def process_data(data: list[str]) -> list[Game]:
    return [process_line_of_data(line) for line in data]


def solve_part1(data, tuples):
    data = process_data(data)
    ids = [game.id_game_possible(tuples) for game in data]
    return sum(ids)


def solve_part2(data):
    data = process_data(data)
    powers = [game.set_power() for game in data]
    return sum(powers)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/Day02/input02.txt")
    color_nums = [("red", 12), ("green", 13), ("blue", 14)]
    print(f'Part 1 solution: {solve_part1(data_input, color_nums)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
