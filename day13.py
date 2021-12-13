from operator import itemgetter

# data = '''6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5'''.split('\n\n')

with open('day13_input.txt') as f:
    data = f.read().split('\n\n')


points, folds = data
points = [tuple(map(int, point.split(','))) for point in points.split()]
folds = [fold.split()[-1] for fold in folds.split('\n')]
grid = {complex(i, j): True for i, j in points}


def print_grid(grid, width=None, height=None):
    if not width:
        width, _ = sorted(points)[-1]
    if not height:
        _, height = sorted(points, key=itemgetter(1))[-1]
    for y in range(height+1):
        for x in range(width+1):
            if grid.get(complex(x, y)):
                print('#', end='')
            else:
                print(' ', end='')
        print()


def fold(grid, instruction):
    """y=7"""
    direction, idx = instruction
    if direction == 'y':
        for pos in grid.copy():
            if int(pos.imag) > idx:
                del grid[pos]
                grid[complex(pos.real, idx-(pos.imag-idx))] = True
    elif direction == 'x':
        for pos in grid.copy():
            if int(pos.real) > idx:
                del grid[pos]
                grid[complex(idx - (pos.real - idx), pos.imag)] = True
    return grid


for i, f in enumerate(folds):
    direction, idx = f.split('=')
    grid = fold(grid, (direction, int(idx)))
    if i == 0:
        print(len(grid))

print_grid(grid, height=5, width=38)

chars = '''#    ###   ##  ###  ###  ####  ##  ### 
#    #  # #  # #  # #  # #    #  # #  #
#    #  # #    #  # #  # ###  #    ### 
#    ###  # ## ###  ###  #    #    #  #
#    # #  #  # #    # #  #    #  # #  #
#### #  #  ### #    #  # ####  ##  ### '''