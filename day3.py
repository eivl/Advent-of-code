from math import prod


with open('day3_input.txt') as f:
    result = f.readlines()
map_ = [line.strip() for line in result]


def is_tree_at_pos(map_, x_pos, y_pos):
    x_mod, y_mod = len(map_), len(map_[0])
    x_map = x_pos % x_mod
    y_map = y_pos % y_mod

    if map_[x_map][y_map] == '#':
        return True
    else:
        return False


def count_trees(map_, x_slope, y_slope):
    count = 0
    current_x, current_y = 0, 0
    while True:
        if current_x > len(map_)-2:
            return count

        current_x += x_slope
        current_y += y_slope

        count += is_tree_at_pos(map_, current_x, current_y)

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
print(prod([count_trees(map_, x, y) for x, y in slopes]))