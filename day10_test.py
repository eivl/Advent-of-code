from math import inf
from scipy.optimize import minimize
import re

with open('day10_input.txt') as f:
    content = f.readlines()


def box_dimensions(time):
    min_x, max_x, min_y, max_y = inf, -inf, inf, -inf
    for x, y, vx, vy in points:
        new_x, new_y = x + time*vx, y + time*vy
        max_x, max_y = max(max_x, new_x), max(max_y, new_y)
        min_x, min_y = min(min_x, new_x), min(min_y, new_y)



    width = max_x - min_x + 1
    height = max_y - min_y + 1
    return width, height, min_x, min_y

def box_area(seconds):
    width, height, *_ = box_dimensions(seconds)
    print(seconds)
    return width * height

points = set()
for line in content:
    numbers = re.findall(r'-?\d+', line)
    x, y, vx, vy = (int(n) for n in numbers)
    points.add((x, y, vx, vy))

result = minimize(box_area, 1)
seconds = int(round(result.x[0]))
width, height, min_x, min_y = box_dimensions(seconds)

text = [['.'] * width for _ in range(height)]
for x, y, vx, vy in points:
    i = x + seconds * vx - min_x
    j = y + seconds * vy - min_y
    text[j][i] = '#'

for line in text:
    print(''.join(line))
print(seconds)
