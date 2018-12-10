from dataclasses import dataclass
from math import inf
import re

with open('day10_input.txt') as f:
    content = f.readlines()

@dataclass
class MyPoint:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int

    def step(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

HEIGHT = 10
drawing_set = set()
points = []

for line in content:
    (pos_x, pos_y, vel_x, vel_y) = re.findall(r"-?\d+", line)
    points.append(MyPoint(int(pos_x), int(pos_y), int(vel_x), int(vel_y)))
    drawing_set.add((int(pos_x), int(pos_y), int(vel_x), int(vel_y)))


def box_dimension(time):
    min_x, max_x, min_y, max_y = inf, -inf, inf, -inf
    for x, y, vx, vy in drawing_set:
        new_x, new_y = x + time*vx, y + time*vy
        max_x, max_y = max(max_x, new_x), max(max_y, new_y)
        min_x, min_y = min(min_x, new_x), min(min_y, new_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    return width, height, min_x, min_y

seconds = 0

while True:
    y = []

    for point in points:
        point.step()
        y.append(point.pos_y)

    seconds += 1

    if max(y) - min(y) <= HEIGHT:
        break

width, height, min_x, min_y = box_dimension(seconds)
text = [[' '] * width for _ in range(height)]
for pos_x, pos_y, vel_x, vel_y in drawing_set:
    i = pos_x + seconds * vel_x - min_x
    j = pos_y + seconds * vel_y - min_y
    text[j][i] = '#'

for line in text:
    print(''.join(line))
print(seconds)

