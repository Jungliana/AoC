class Game:
    def __init__(self, game_id: int, games: list[list[tuple]]) -> None:
        self.id = game_id
        self.games = games

    def __str__(self) -> str:
        return f'Game: {self.id}'

    def id_game_possible(self, all_cubes: list[tuple]) -> int:
        for example in self.games:
            for color in example:
                for cubes in all_cubes:
                    if (color[0] == cubes[0]) and (color[1] > cubes[1]):
                        return 0
        return self.id


def read_data(path: str) -> list[str]:
    with open(path, encoding="ASCII") as file:
        lines = file.readlines()
    return lines


def process_line_of_data(line: str) -> Game:
    # Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green; 11 green, 6 blue; 8 blue, 12 green
    games = line.rstrip("\n").split(":")
    game_id = int(games[0].split()[1])
    games_splitted = games[1].split(";")
    all_games = []
    for game in games_splitted:
        cubes = game.split(",")
        all_games.append([(details.split()[1], int(details.split()[0])) for details in cubes])
    # [[(10, "green"), (9, "blue"), (1, "red")], [(1, "red"), (7, "green")]]
    return Game(game_id, all_games)


def process_data(data: list[str]) -> list[Game]:
    return [process_line_of_data(line) for line in data]


def solve_part1(data, tuples):
    data = process_data(data)
    ids = [game.id_game_possible(tuples) for game in data]
    print(ids)
    return sum(ids)


def solve_part2(data):
    pass


if __name__ == "__main__":
    data_input = read_data("AoC-2023/Day02/input02.txt")
    print(f'Part 1 solution: {solve_part1(data_input, [("red", 12), ("green", 13), ("blue", 14)])}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
