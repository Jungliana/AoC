"""Day06 - puzzle solutions for day 06."""


def load_data(path: str) -> str:
    """Load and split data from file."""
    with open(path, encoding="ascii") as file:
        return file.readlines()[0]


def all_charas_different(token):
    return (token[0] not in token[1:]) and (token[-1] not in token[:-1]) and (token[1] != token[2])


def solve_part1(stream):
    que = list(stream[0:4])
    counter = 4
    if all_charas_different(que):
        return counter
    for character in stream[4:]:
        counter += 1
        que.pop(0)
        que.append(character)
        if all_charas_different(que):
            return counter
    return counter


if __name__ == "__main__":
    data = load_data("Day06/input06.txt")
    print(f'Part 1 answer: {solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
