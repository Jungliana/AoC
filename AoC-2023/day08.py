from math import gcd


def read_data(path: str) -> list[list[str]]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(line.rstrip().split(" = "))
    return lines[0][0], lines[2:]  # hints, nodes


def build_node_dict(nodes) -> dict:
    node_dict = {}
    for line in nodes:
        left_right = line[1].lstrip('(').rstrip(')').split(', ')
        node_dict.update({line[0]: (left_right[0], left_right[1])})
    return node_dict


def solve_part1(hints, node_dict) -> int:
    return count_steps(node_dict, hints, 'AAA')


def count_steps(node_dict, hints, node) -> int:
    current_node = node
    counter = 0

    while current_node[2] != 'Z':
        for letter in hints:
            if letter == 'L':
                current_node = node_dict[current_node][0]
            else:
                current_node = node_dict[current_node][1]
            counter += 1
    return counter


def solve_part2(hints, node_dict) -> int:
    starting_nodes = list(filter(lambda x: x[2] == 'A', node_dict.keys()))
    counters = [count_steps(node_dict, hints, node) for node in starting_nodes]

    lcm = 1
    for i in counters:
        lcm = lcm*i // gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    data_hints, data_nodes = read_data("AoC-2023/inputs/input08.txt")
    data_node_dict = build_node_dict(data_nodes)
    print(f'Part 1 solution: {solve_part1(data_hints, data_node_dict)}')
    print(f'Part 2 solution: {solve_part2(data_hints, data_node_dict)}')
