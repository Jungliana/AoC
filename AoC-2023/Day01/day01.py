
def read_data(path: str) -> list[str]:
    with open(path) as file:
        lines = file.readlines()
    return lines


def find_integers(data: list[str]) -> list[list[int]]:
    return [list(map(int, filter(str.isdigit, [*line]))) for line in data]


def sum_integers(data: list[list[int]]) -> int:
    return sum(10 * line[0] + line[-1] for line in data)


def solve_part1(data: list[str]) -> int:
    return sum_integers(find_integers(data))


if __name__ == "__main__":
    data = read_data("AoC-2023/Day01/input01.txt")
    print(solve_part1(data))
