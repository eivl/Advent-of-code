import itertools as it
from collections import defaultdict, namedtuple, Counter
from copy import deepcopy

class Square(namedtuple('Square', 'x y')):
    def __add__(self, other):
        return Square(self.x + other.x, self.y + other.y)

with open('day18_input.txt') as f:
    content = f.read().split('\n')

'''
0 = Open -> -
1 = tree -> |
11 = lumberyard -> #

if square == 0 : return 1 if adj_square == 3-8
if square == 1 : return 11 if adj_square >= 33
if square == 11: return 11 if adj_square = min 11+1 -> else: 0

'''

SIZE = 50
ADJ = {Square(-1, -1), Square(-1, 0), Square(-1, 1), Square(0, -1), Square(0, 1), Square(1, -1), Square(1, 0), Square(1, 1)}


acre = defaultdict(lambda: 0)
for y in range(len(content)):
    for x in range(len(content[y])):
        if content[y][x] == '.':
            acre[Square(x, y)] = 0
        elif content[y][x] == '|':
            acre[Square(x, y)] = 1
        elif content[y][x] == '#':
            acre[Square(x, y)] = 11
        else:
            print('Something strange')

def count_adj(square):
    x, y = map(int, square)
    _sum = []
    for adj_square in ADJ:
        _sum.append(acre[Square(x, y) + adj_square])
    return sum(_sum)

def draw_map(acres):
    _map = [[0]*SIZE for _ in range(SIZE)]
    for x, y in it.product(range(SIZE), range(SIZE)):
        if acres[Square(x, y)] == 0:
            _map[x][y] = '.'
        elif acres[Square(x, y)] == 1:
            _map[x][y] = '|'
        elif acres[Square(x, y)] == 11:
            _map[x][y] = '#'
    return ''.join([''.join([str(c) for c in lst]) for lst in _map])

acre_time = 410 # repeating cycle estimate
previous = []
for _ in range(16):
    for i in range(acre_time):
        backup = deepcopy(acre)
        for x, y in it.product(range(SIZE), range(SIZE)):
            count = count_adj((x, y))
            if acre[Square(x, y)] == 0:
                if count % 11 >= 3:
                    backup[Square(x, y)] = 1
            elif acre[Square(x, y)] == 1:
                if count >= 33:
                    backup[Square(x, y)] = 11
            elif acre[Square(x, y)] == 11:
                if count >= 12 and count % 11 > 0:
                    backup[Square(x, y)] = 11
                else:
                    backup[Square(x, y)] = 0
        acre = backup


    c = Counter((acre[Square(x, y)] for x, y in it.product(range(SIZE), range(SIZE))))


    # from textwrap import wrap
    # w = wrap(draw_map(acre), 50)
    # print(w)
    # c = Counter(list_of_data)

    value = c[1]*c[11]
    if value in previous:
        break
    previous.append(value)

    print(_, (c[1], c[11]), c[1]*c[11]) # find part2 manually, no time left



# (81, (651, 358), 233058)
# (82, (616, 341), 210056)
# (83, (606, 352), 213312)
# (84, (648, 351), 227448)
# (85, (613, 339), 207807)
# (86, (613, 368), 225584)
# (87, (638, 347), 221386)
# (88, (610, 338), 206180)
# (89, (628, 371), 232988)
# (90, (628, 344), 216032)
# (91, (607, 337), 204559)
# (92, (644, 363), 233772)
# (93, (620, 341), 211420)
# (94, (604, 343), 207172)
# (95, (651, 358), 233058)
# (96, (616, 341), 210056)
# (97, (606, 352), 213312)
# (98, (648, 351), 227448)
# (99, (613, 339), 207807)
# (100, (613, 368), 225584)
# (101, (638, 347), 221386)
# (102, (610, 338), 206180)
# (103, (628, 371), 232988)
# (104, (628, 344), 216032)
# (105, (607, 337), 204559)
# (106, (644, 363), 233772)
# (107, (620, 341), 211420)
# (108, (604, 343), 207172)
# (109, (651, 358), 233058)
# (110, (616, 341), 210056)
# (111, (606, 352), 213312)
# (112, (648, 351), 227448)
# (113, (613, 339), 207807)
# (114, (613, 368), 225584)
# (115, (638, 347), 221386)
