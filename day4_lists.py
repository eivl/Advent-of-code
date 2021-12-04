from itertools import chain
from time import perf_counter

start = perf_counter()

with open('day4_input.txt') as f:
    numbers, *boards = f.read().split('\n\n')

numbers = [int(num) for num in numbers.split(',')]
boards = [[[int(num) for num in line.split()]
           for line in board.split('\n')]
          for board in boards]
BOARD_LENGTH = len(boards)


def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)


winners = set()
possible_indexes = set(range(BOARD_LENGTH))

for number in numbers:
    for board_idx in possible_indexes.difference(winners):
        for row_idx, row in enumerate(boards[board_idx]):
            for num_idx, num in enumerate(row):
                if number == num:
                    row[num_idx] = 0
                    column = [col for col in zip(*boards[board_idx])][num_idx]
                    if not sum(row) or not sum(column):
                        winners.add(board_idx)
                        if len(winners) == 1:
                            print(sum(flatten(boards[board_idx])) * num)

                        if len(winners) == len(boards):
                            print(sum(flatten(boards[board_idx])) * num)

end = perf_counter()
print(end - start)
