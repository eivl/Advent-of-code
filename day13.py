import names
import numpy as np
import copy
from dataclasses import dataclass, field
from itertools import cycle
from operator import itemgetter
from typing import Any


with open('day13_input.txt') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
_map = np.zeros((len(content), len(content[0])), dtype=object)

carts = []
for i, line in enumerate(content):
    for j, square in enumerate(line):
        if square == ' ':
            continue
        elif square == '-':
            _map[i, j] = 1
        elif square == '|':
            _map[i, j] = 2
        elif square == '/':
            _map[i, j] = 3
        elif square == '\\':
            _map[i, j] = 4
        elif square == '+':
            _map[i, j] = 5
        elif square == '>':
            _map[i, j] = 1
            carts.append([1, i, j])
        elif square == '<':
            _map[i, j] = 1
            carts.append([3, i, j])
        elif square == '^':
            _map[i, j] = 2
            carts.append([0, i, j])
        elif square == 'v':
            _map[i, j] = 2
            carts.append([2, i, j])
        else:
            raise Exception('Something went wrong')

@dataclass
class Map:
    _map: np.ndarray

    def __post_init__(self):
        self.length = len(self._map[0])
        self.height = len(self._map)


@dataclass
class Cart(Map):
    name: Any # to be removed later
    facing_direction: int # 0 = North, 1 = East, 2 = South, 3 = West
    x_pos: int
    y_pos: int
    wheel: Any = None
    sort_index: int = field(init=False, repr=False)

    def __post_init__(self):
        self.c = cycle(('left', 'straight', 'right'))
        self.wheel = next(self.c)
        super().__post_init__()
        self.sort_index = self.x_pos*self.length + self.y_pos

    def __lt__(self, other):
        return self.x_pos*self.length + self.y_pos < other.x_pos*other.length + other.y_pos

    def turn_wheel(self):
        self.wheel = next(self.c)

    def whats_ahead(self):
        if self.facing_direction == 0:
            self.ahead = self._map[self.x_pos-1][self.y_pos]
        elif self.facing_direction == 1:
            self.ahead = self._map[self.x_pos][self.y_pos+1]
        elif self.facing_direction == 2:
            self.ahead = self._map[self.x_pos+1][self.y_pos]
        elif self.facing_direction == 3:
            self.ahead = self._map[self.x_pos][self.y_pos-1]
        else:
            raise Exception('Nothing ahead')

    def swap(self):
        if self.ahead == 3:
            if self.facing_direction == 0 or facing_direction == 1:
                self.facing_direction = (1,0)[self.facing_direction]
            else:
                self.facing_direction = (3,2)[self.facing_direction%2]


    def move(self):
        self.whats_ahead()
        self.move_cart()
        if self.ahead == 3: # /
            if self.facing_direction == 0 or self.facing_direction == 1:
                self.facing_direction = (1,0)[self.facing_direction]
            else:
                self.facing_direction = (3,2)[self.facing_direction%2]

        elif self.ahead == 4: # \
            if self.facing_direction == 0 or self.facing_direction == 3:
                self.facing_direction = (3,0)[self.facing_direction//3]
            else:
                self.facing_direction = (0,2,1)[self.facing_direction%3]

        elif self.ahead == 5: # +
            if self.wheel == 'left':
                self.facing_direction = (self.facing_direction+3) % 4
            elif self.wheel == 'straight':
                # handle straight
                pass
            elif self.wheel == 'right':
                self.facing_direction = (self.facing_direction+1) % 4
            self.turn_wheel()
        # backup = copy.deepcopy(self._map)
        # backup[self.x_pos][self.y_pos] = self.decode_fd()
        # print('#'*self.length)
        # for l in backup:
        #     print(l)
        # print('#'*self.length)

    def decode_fd(self):
        if self.facing_direction == 0:
            return '^'
        elif self.facing_direction == 1:
            return '>'
        elif self.facing_direction == 2:
            return 'v'
        elif self.facing_direction == 3:
            return '<'

    def move_cart(self):
        if self.facing_direction == 0:
            self.x_pos = self.x_pos - 1
        elif self.facing_direction == 1:
            self.y_pos = self.y_pos + 1
        elif self.facing_direction == 2:
            self.x_pos = self.x_pos + 1
        elif self.facing_direction == 3:
            self.y_pos = self.y_pos - 1
        else:
            raise Exception('Cannot move in that direction')

my_carts = []
for c in carts:
    my_carts.append(Cart(_map, names.get_first_name(), c[0], c[1], c[2]))
my_carts = sorted(my_carts)

def check_collision(carts):
    pos = [(c.y_pos, c.x_pos) for c in my_carts]
    if len(set(pos)) == len(my_carts)-1:
        x, y = list(set(pos))[0]
        print(f'{x},{y}')
        return True
    return False


for i in range(200):
    for c in my_carts:
        c.move()
        if check_collision(my_carts):
            break
    if check_collision(my_carts):
        break



