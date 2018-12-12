from itertools import product
from operator import itemgetter
from collections import defaultdict
from math import inf

SERIAL = 8979
GRID_SIZE = 300
def power_level(x, y, serial=SERIAL):
    return ((((x+10)*y + serial) * (x+10)//100)%10)-5

board = []
row = []
for i, coord in enumerate(product(range(1, GRID_SIZE+1), range(1, GRID_SIZE+1)),start=1):
    row.append(power_level(*coord))
    if i % GRID_SIZE == 0:
        board.append(row[:])
        row.clear()


def find_largest_slice(board, slicesize=3):
    highest_sum = -inf
    slice_coord = (0,0)
    for i in range(GRID_SIZE-slicesize):
        for j in range(GRID_SIZE-slicesize):
            board_slice = []
            if j+slicesize < GRID_SIZE:
                for bs in range(slicesize):
                    try:
                        board_slice.extend(board[i+bs][j:j+slicesize])
                    except IndexError:
                        break
            current_sum = sum(board_slice)
            if current_sum > highest_sum:
                highest_sum = current_sum
                x, y = (i+1, j+1 )

    return (x, y, highest_sum)

print(find_largest_slice(board))

# result = []
# for s in range(1, 301):
#     x, y, hsum = find_largest_slice(board, slicesize=s)
#     result.append((x, y, s, hsum))
#     print(f'Done {s}x{s}, continueing')
# x, y, s, _ = max(result, key=itemgetter(3))
# print(x, y, s)


# optimazation and testing

def make_1d_board():
    return[power_level(*coord) for i, coord in enumerate(product(range(1, GRID_SIZE+1), range(1, GRID_SIZE+1)),start=1)]

def my_slice(board, start=0, slicesize=3):
    my_board = []
    for s in range(slicesize):
        my_board.extend(board[start+(s*GRID_SIZE):start+slicesize+(s*GRID_SIZE)])
    return sum(my_board)

def find_largest_slice2(board, slicesize=3):
    result = []
    for i, _ in enumerate(board):
        result.append((i // GRID_SIZE,
                       i % GRID_SIZE,
                       my_slice(board, start=i, slicesize=slicesize)))
    return max(result, key=itemgetter(2))

print(find_largest_slice(board))
my_board = make_1d_board()
### still to slow.. testing memoization later
