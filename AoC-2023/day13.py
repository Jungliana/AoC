from itertools import groupby


def read_data(path: str) -> list[list[str]]:
    lines = []
    rows = []
    columns = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(line.rstrip())
    rows = [list(g) for k, g in groupby(lines, key=lambda x: x == '') if not k]
    for row in rows:
        cols_from_rows = []
        for i in range(len(row[0])):
            column = ''
            for element in row:
                column += element[i]
            cols_from_rows.append(column)
        columns.append(cols_from_rows)
    return rows, columns


def find_mirror_line(rows: list[str]):
    for i in range(len(rows) - 1):
        if rows[i] == rows[i+1]:
            idx1 = i
            idx2 = i+1
            while (idx1 >= 0) and (idx2 < len(rows)) and (rows[idx1] == rows[idx2]):
                idx1 -= 1
                idx2 += 1
            if (idx1 == -1) or idx2 == (len(rows)):
                return i + 1
    return 0


def solve_part1(rows: list[list[str]], columns: list[list[str]]) -> int:
    sum_rows_cols = 0
    for row in rows:
        sum_rows_cols += 100 * find_mirror_line(row)
    for col in columns:
        sum_rows_cols += find_mirror_line(col)
    return sum_rows_cols


def solve_part2(data: list[list[str]], columns: list[list[str]]) -> int:
    return 0


if __name__ == "__main__":
    data_rows, data_columns = read_data("AoC-2023/inputs/input13.txt")
    print(f'Part 1 solution: {solve_part1(data_rows, data_columns)}')
    print(f'Part 2 solution: {solve_part2(data_rows, data_columns)}')
