from shapely.geometry import Polygon, Point


def read_data(path: str) -> "PipeMatrix":
    pipe_cols = []
    with open(path, encoding="ASCII") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        pipe_cols.append([Pipe(
            line, (j, i)) for j, line in enumerate(lines[i].rstrip())])
    return PipeMatrix(pipe_cols)


class Pipe:
    SHAPE = {
        "|": (1, 0, 0, 1),  # N, E, W, S
        "-": (0, 1, 1, 0),
        "L": (1, 1, 0, 0),
        "J": (1, 0, 1, 0),
        "7": (0, 0, 1, 1),
        "F": (0, 1, 0, 1),
        ".": (0, 0, 0, 0),
        "S": (1, 1, 1, 1)
    }

    def __init__(self, p_type: str, x_y: tuple[int]) -> None:
        self.type = p_type
        self.shape = self.SHAPE[self.type]
        self.coords = x_y

        self.steps = 1000000
        self.come_from = 0

    def find_next(self) -> int:
        for i in range(4):
            if self.shape[i] == 1 and i != self.come_from:
                return i

    def __str__(self) -> str:
        return f'{self.type}'

    def __lt__(self, other: "Pipe") -> bool:
        return self.steps < other.steps

    def __gt__(self, other: "Pipe") -> bool:
        return self.steps > other.steps


class PipeMatrix:
    VERTICES = ["F", "J", "L", "7"]

    def __init__(self, matrix: list[list[Pipe]]) -> None:
        self.matrix = matrix
        self.x_size: int = len(self.matrix[0])
        self.y_size: int = len(self.matrix)
        self.start: Pipe = self.find_start()
        self.define_start_shape()

        self.loop_vertices = []

    def find_start(self) -> Pipe:
        return next(filter(lambda x: x.type == "S", self.flatten()))

    def define_start_shape(self) -> None:
        x, y = self.start.coords[0], self.start.coords[1]
        north = self.matrix[y-1][x].shape[3] if y > 0 else 0
        east = self.matrix[y][x+1].shape[2] if x+1 < self.x_size else 0
        west = self.matrix[y][x-1].shape[1] if x > 0 else 0
        south = self.matrix[y+1][x].shape[0] if y+1 < self.y_size else 0

        dirs = (north, east, west, south)
        self.start.shape = dirs
        key_list = list(Pipe.SHAPE.keys())
        val_list = list(Pipe.SHAPE.values())

        position = val_list.index(dirs)
        self.start.type = key_list[position]

    def loopey_loop(self) -> None:
        for i, value in enumerate(self.start.shape):
            if value == 1:
                self.loop_vertices = []
                current = self.start
                if current.type in self.VERTICES:
                    self.loop_vertices.append(current.coords)
                self.start.come_from = i
                counter = 1
                current = self.next_pipe(self.start)
                current.steps = counter

                while current != self.start:
                    counter += 1
                    if current.type in self.VERTICES:
                        self.loop_vertices.append(current.coords)
                    current = self.next_pipe(current=current)
                    if current != self.start:
                        current.steps = min(current.steps, counter)

    def next_pipe(self, current: Pipe) -> Pipe:
        next_dir = current.find_next()
        if next_dir == 0:
            pipe = self.matrix[current.coords[1]-1][current.coords[0]]
        elif next_dir == 1:
            pipe = self.matrix[current.coords[1]][current.coords[0]+1]
        elif next_dir == 2:
            pipe = self.matrix[current.coords[1]][current.coords[0]-1]
        else:
            pipe = self.matrix[current.coords[1]+1][current.coords[0]]
        pipe.come_from = 3-next_dir
        return pipe

    def flatten(self) -> list[Pipe]:
        flat_list = []
        for row in self.matrix:
            flat_list.extend(row)
        return flat_list

    def __str__(self) -> str:
        return f'PipeMatrix, x size = {self.x_size}, y size = {self.y_size}'


def solve_part1(data: PipeMatrix) -> int:
    data.loopey_loop()
    return max(filter(lambda x: x.steps < 1000000, data.flatten())).steps


def count_points_inside_polygon(vertices):
    polygon = Polygon(vertices)
    min_x, min_y, max_x, max_y = polygon.bounds
    grid_points = [(x, y) for x in range(int(min_x), int(max_x) + 1) for y in range(int(min_y), int(max_y) + 1)]

    n = 0
    for point in grid_points:
        if polygon.contains(Point(point)):
            n += 1
    return n


def solve_part2(data: PipeMatrix) -> int:
    data.loopey_loop()
    return count_points_inside_polygon(data.loop_vertices)


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input10.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
