import copy
import re
from collections import deque

with open('day5_input.txt') as f:
    result = f.read()


init, rules = result.split('\n\n')

original_grid = []
for column in zip(*init.split('\n')):
    if column[-1].isdigit():
        original_grid.append(deque(''.join(column).strip()[:-1]))


def move(from_col: deque, to_col: deque, num: int = 1, part_one=True):
    if part_one:
        for _ in range(num):
            to_col.extendleft(from_col.popleft())
        return
    elif num == 1:
        to_col.extendleft(from_col.popleft())
    else:
        tmp = deque()
        for _ in range(num):
            tmp.appendleft(from_col.popleft())
        to_col.extendleft(tmp)


def print_answer(queue):
    tmp_queue = copy.deepcopy(queue)
    return ''.join([row.popleft() for row in tmp_queue])


def part_one(grid):
    for rule in rules.splitlines():
        number, fromcol, tocol = (int(num) for num in re.findall('[0-9]+', rule))
        move(grid[fromcol-1], grid[tocol-1], number)

    return print_answer(grid)


def part_two(grid):
    for rule in rules.splitlines():
        number, fromcol, tocol = (int(num) for num in re.findall('[0-9]+', rule))
        move(grid[fromcol-1], grid[tocol-1], number, part_one=False)
    return print_answer(grid)


my_grid = copy.deepcopy(original_grid)
print(part_one(my_grid))
my_grid = copy.deepcopy(original_grid)
print(part_two(my_grid))

