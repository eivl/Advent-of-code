# from itertools import product
# from operator import itemgetter
# from collections import defaultdict
# from math import inf

# SERIAL = 8979
# GRID_SIZE = 300
# def power_level(x, y, serial=SERIAL):
#     return ((((x+10)*y + serial) * (x+10)//100)%10)-5

# board = []
# row = []
# for i, coord in enumerate(product(range(1, GRID_SIZE+1), range(1, GRID_SIZE+1)),start=1):
#     row.append(power_level(*coord))
#     if i % GRID_SIZE == 0:
#         board.append(row[:])
#         row.clear()


# def find_largest_slice(board, slicesize=3):
#     highest_sum = -inf
#     slice_coord = (0,0)
#     for i in range(GRID_SIZE-slicesize):
#         for j in range(GRID_SIZE-slicesize):
#             board_slice = []
#             if j+slicesize < GRID_SIZE:
#                 for bs in range(slicesize):
#                     try:
#                         board_slice.extend(board[i+bs][j:j+slicesize])
#                     except IndexError:
#                         break
#             current_sum = sum(board_slice)
#             if current_sum > highest_sum:
#                 highest_sum = current_sum
#                 x, y = (i+1, j+1 )

#     return (x, y, highest_sum)

# print(find_largest_slice(board))

# # result = []
# # for s in range(1, 301):
# #     x, y, hsum = find_largest_slice(board, slicesize=s)
# #     result.append((x, y, s, hsum))
# #     print(f'Done {s}x{s}, continueing')
# # x, y, s, _ = max(result, key=itemgetter(3))
# # print(x, y, s)


# # optimazation and testing

# def make_1d_board():
#     return[power_level(*coord) for i, coord in enumerate(product(range(1, GRID_SIZE+1), range(1, GRID_SIZE+1)),start=1)]

# def my_slice(board, start=0, slicesize=3):
#     my_board = []
#     for s in range(slicesize):
#         my_board.extend(board[start+(s*GRID_SIZE):start+slicesize+(s*GRID_SIZE)])
#     return sum(my_board)


# def find_largest_slice2(board, slicesize=3):
#     result = []
#     for i, _ in enumerate(board):
#         result.append((i // GRID_SIZE,
#                        i % GRID_SIZE,
#                        my_slice(board, start=i, slicesize=slicesize)))
#     return max(result, key=itemgetter(2))

# print(find_largest_slice(board))
# my_board = make_1d_board()



from functools import lru_cache

serial = 8979

max_power = 0
max_power_coords = None


@lru_cache(None)
def calc_power(x, y, size):
    global max_power, max_power_coords

    if size == 1:  # single field
        rack_id = x + 10
        power_lv = (rack_id * y + serial) * rack_id
        power = power_lv % 1000 // 100 - 5

    else:  # split the square in four partial squares
        if size % 2:
            # odd square size: make two bigger and two smaller squares and
            # subtract the intersecting center field otherwise counted twice
            half = size // 2
            power = (
                calc_power(x, y, half + 1) +
                calc_power(x + half + 1, y, half) +
                calc_power(x, y + half + 1, half) +
                calc_power(x + half, y + half, half + 1) +
                -calc_power(x + half, y + half, 1)
            )
        else:
            # even square size: four equally sized partial squares
            half = size // 2
            power = (
                calc_power(x, y, half) +
                calc_power(x + half, y, half) +
                calc_power(x, y + half, half) +
                calc_power(x + half, y + half, half)
            )

    if power > max_power:
        max_power, max_power_coords = power, (x, y, size)
        # print(max_power, max_power_coords)

    return power


print(f"Progress: {0:3}%", end="")

for size in range(1, 301):
    if not size % 3:
        print(f"\rProgress: {size // 3:3}%", end="")
    for x in range(1, 302 - size):
        for y in range(1, 302 - size):
            calc_power(x, y, size)

print(end="\r")
# print(calc_power.cache_info())

print(f"The highest powered square has {max_power} total power "
      f"and the coordinates/size {','.join(map(str, max_power_coords))}.")
