import sys
from collections import defaultdict
from operator import itemgetter
from timeit import default_timer as timer

start = timer()

sys.setrecursionlimit(2500)
with open('day17_input.txt') as f:
    content = f.readlines()

clay = defaultdict(bool)

for line in content:
    coord, _range = line.split(',')
    if coord[0] == 'x':
        x = int(coord.split('=')[1])
        y1, y2 = map(int, _range[3:].split('..'))

        for y in range(y1, y2 + 1):
            clay[(x, y)] = True
    else:
        y = int(coord.split('=')[1])
        x1, x2 = map(int, _range[3:].split('..'))

        for x in range(x1, x2 + 1):
            clay[(x, y)] = True

ymin, ymax = min(clay, key=itemgetter(1))[1], max(clay, key=itemgetter(1))[1]

settled = set()
flowing = set()



def fill(square, direction=(0, 1)):
    flowing.add(square)

    below = (square[0], square[1] + 1)

    if not clay[below] and below not in flowing and 1 <= below[1] <= ymax:
        fill(below)

    if not clay[below] and below not in settled:
        return False

    left = (square[0] - 1, square[1])
    right = (square[0] + 1, square[1])
    left_filled = clay[left] or left not in flowing and fill(left, direction=(-1, 0))
    right_filled = clay[right] or right not in flowing and fill(right, direction=(1, 0))
    if direction == (0, 1) and left_filled and right_filled:
        settled.add(square)

        while left in flowing:
            settled.add(left)
            left = (left[0] - 1, left[1])

        while right in flowing:
            settled.add(right)
            right = (right[0] + 1, right[1])

    return direction == (-1, 0) and (left_filled or clay[left]) or \
        direction == (1, 0) and (right_filled or clay[right])

fill((500, 0))

ss = []
for s in flowing:
    if ymin <= s[1]  and s[1]<= ymax:
        ss.append(s)




sss = []
for s in settled:
    if ymin <= s[1]  and s[1]<= ymax:
        sss.append(s)
end = timer()

print(end-start)
print('part1:', len(ss))
print('part2:', len(sss))
