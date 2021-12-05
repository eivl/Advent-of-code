from collections import namedtuple, defaultdict

with open('day5_input.txt') as f:
    result = f.readlines()
result = [line.replace('->', ',') for line in result]

# result = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''.replace(' -> ', ',').splitlines()


Point = namedtuple('Point', ['x', 'y'])

grid = defaultdict(int)


def not_diagonal(line):
    x1, y1, x2, y2 = line
    return x1 == x2 or y1 == y2


def make_line(line):
    x1, y1, x2, y2 = line
    if diff := x2 - x1:
        if abs(diff) != diff:
            x2, x1 = x1, x2
        for i in range(abs(diff)+1):
            grid[Point(x1+i, y1)] += 1
    elif diff := y2 - y1:
        if abs(diff) != diff:
            y2, y1 = y1, y2
        for i in range(abs(diff)+1):
            grid[Point(x1, y1+i)] += 1


def make_diagonal_line(line):
    x1, y1, x2, y2 = line
    x_diff = x2 - x1
    x_range = range(x1, x2 + 1)
    y_diff = y2 - y1
    y_range = range(y1, y2 + 1)
    if abs(x_diff) != x_diff:
        x_range = range(x2, x1 + 1)[::-1]
    if abs(y_diff) != y_diff:
        y_range = range(y2, y1 + 1)[::-1]
    for x, y in zip(x_range, y_range):
        grid[Point(x, y)] += 1


def solution(part_2=False):
    grid.clear()
    for line in result:
        line = [int(num) for num in line.split(',')]
        if not_diagonal(line):
            make_line(line)
        else:
            if part_2:
                make_diagonal_line(line)

    return sum(num > 1 for num in grid.values())


print(solution())
print(solution(part_2=True))

