from itertools import cycle, islice
import collections


def consume(iterator, n=None):
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


ROCK = 1
PAPER = 2
SCISSOR = 3
WIN = 6
DRAW = 3
LOSE = 0

with open('day2_input.txt') as f:
    result = f.read().splitlines()


def part_one():
    status_cycle = cycle((DRAW, WIN, LOSE))
    order_cycle = cycle((ROCK, PAPER, SCISSOR))

    rules = {}
    for first in 'ABC':
        for second in 'XYZ':
            rules[f'{first} {second}'] = next(status_cycle) + next(order_cycle)
        consume(status_cycle, 2)
    return sum(rules[game] for game in result)


def part_two():
    status_cycle = cycle((LOSE, DRAW, WIN))
    order_cycle = cycle((SCISSOR, ROCK, PAPER))

    rules = {}
    for first in 'ABC':
        for second in 'XYZ':
            rules[f'{first} {second}'] = next(status_cycle) + next(order_cycle)
        consume(order_cycle, 1)
    return sum(rules[game] for game in result)


print(part_one())
print(part_two())
