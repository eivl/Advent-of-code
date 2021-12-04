from dataclasses import dataclass, field
from typing import ClassVar
from time import perf_counter

start = perf_counter()

with open('day4_input.txt') as f:
    numbers = [int(num) for num in f.readline().split(',')]
    data = f.read().split('\n\n')


@dataclass
class Number:
    number: int
    marked: bool = False


@dataclass
class Board:
    numbers: ClassVar[list] = []
    board: list[list[Number]] = field(default_factory=list)


boards = []
for board in data:
    element = []
    for line in board.split('\n'):
        if not line:
            continue
        element.append([Number(int(num)) for num in line.split()])
    boards.append(Board(board=element))


def check(board, numbers):
    for row in board:
        for num in row:
            if num.number in numbers:
                num.marked = True
        if all(num.number in numbers for num in row):
            return board

    for column in zip(*board):
        if all(num.number in numbers for num in column):
            return board
    return False


winner = None
for i in range(6, len(numbers)):
    for board in boards[:]:
        checked = check(board.board, numbers[:i])
        if checked:
            winner = (checked, numbers[:i][-1])
    if winner:
        break

board, num = winner
result = [number.number
          for row in board
          for number in row
          if number.marked is False]

print(sum(result)*num)


winner = None
removed = 0
win = []
to_remove = []
for i in range(6, len(numbers)+1):
    for idx, board in enumerate(boards):
        if board is None:
            continue
        checked = check(board.board, numbers[:i+removed])
        if checked:
            winner = (checked, numbers[:i+removed][-1])
            boards[idx] = None


board, num = winner
result = [number.number
          for row in board
          for number in row
          if number.marked is False]

print(sum(result)*num)
end = perf_counter()
print(end-start)