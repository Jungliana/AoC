"""Day06 - puzzle solutions for day 06."""


def load_data(path: str) -> str:
    """Load and split data from file."""
    with open(path, encoding="ascii") as file:
        return file.readlines()[0]


def all_charas_different(token: list) -> bool:
    """Check if every item in a list is different."""
    for i in range(len(token)-1):
        if token[i] in token[i+1:]:
            return False
    return True


def solve(stream: str, length: int) -> int:
    """Solve part 1 and part 2 of the puzzle."""
    que = list(stream[0:length])
    counter = length
    if all_charas_different(que):
        return counter
    for character in stream[length:]:
        counter += 1
        que.pop(0)
        que.append(character)
        if all_charas_different(que):
            return counter
    return counter


if __name__ == "__main__":
    data = load_data("AoC-2022/Day06/input06.txt")
    print(f'Part 1 answer: {solve(data, 4)}')
    print(f'Part 2 answer: {solve(data, 14)}')
