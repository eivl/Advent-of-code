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
a = count_trees(map_, x_slope=1, y_slope=1)
b = count_trees(map_, x_slope=1, y_slope=3)
c = count_trees(map_, x_slope=1, y_slope=5)
d = count_trees(map_, x_slope=1, y_slope=7)
e = count_trees(map_, x_slope=2, y_slope=1)

print(a*b*c*d*e)
