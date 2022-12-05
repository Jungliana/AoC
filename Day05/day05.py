"""Day05 - puzzle solutions for day 05."""


def load_data(path: str) -> list[str]:
    """Load and split data from file."""
    lines = []
    with open(path, encoding="ascii") as file:
        for line in file:
            lines.append(line.split())
    return lines


class Crane():
    """Crane for moving crates."""

    def __init__(self) -> None:
        """Construct a crane with starting crate configuration."""
        self.crates = [
            [],
            ['H', 'C', 'R'],
            ['B', 'J', 'H', 'L', 'S', 'F'],
            ['R', 'M', 'D', 'H', 'J', 'T', 'Q'],
            ['S', 'G', 'R', 'H', 'Z', 'B', 'J'],
            ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B'],
            ['T', 'H', 'C', 'G'],
            ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L'],
            ['R', 'J', 'Q', 'G', 'C'],
            ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
        ]

    def move_crates(self, many: int, m_from: int, m_to: int) -> None:
        """Move x crates from one stack to another."""
        for _ in range(many):
            crate = self.crates[m_from].pop()
            self.crates[m_to].append(crate)

    def move_all(self, lines: list[list[str]]) -> None:
        """Move all crates according to the instructions."""
        for line in lines:
            self.move_crates(int(line[1]), int(line[3]), int(line[5]))

    def read_message(self) -> str:
        """Read message from crate stacks."""
        message = ''
        for i in range(1, 10):
            message += self.crates[i].pop()
        return message

    def solve_part1(self, lines: list[list[str]]) -> str:
        """Solve part 1 of the puzzle."""
        self.move_all(lines)
        return self.read_message()


if __name__ == "__main__":
    data = load_data("Day05/input05_b.txt")
    crane1 = Crane()
    print(f'Part 1 answer: {crane1.solve_part1(data)}')
    # print(f'Part 2 answer: {solve_part2(data)}')
