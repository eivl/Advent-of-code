from dataclasses import dataclass, field
from math import inf
from typing import List
from scipy.optimize import minimize
import numpy as np
import re

with open('day10_input.txt') as f:
    content = f.readlines()

xdata = [int(x[10:16]) for x in content]
ydata = [int(y[18:24]) for y in content]
dxdata = [int(dx[36:38]) for dx in content]
dydata = [int(dy[39:42]) for dy in content]


@dataclass(unsafe_hash=True)
class TwoDPoint:
    x : int
    y : int
    dy: int
    dx: int

    def __iter__(self):
        return iter([self.x, self.y, self.dx, self.dy])

    def current_possition(self, time):
        return (self.x + self.dx*time, self.y + self.dy*time)

@dataclass
class MyPlot:
    points: List[TwoDPoint]
    min_x: float = inf
    min_y: float = inf
    max_x: float = -inf
    max_y: float = -inf
    index : int = 0


    def __iter__(self):
        return self.points

    def __next__(self):
        try:
            result = self.points[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def add_point(self, x, y, dx, dy):
        self.points.append(TwoDPoint(x, y, dx, dy))

    def box_dimension(self, time):
        min_x, max_x, min_y, max_y = inf, -inf, inf, -inf
        for x, y, vx, vy in self.points:
            newx, newy = x + time*vx, y + time*vy
            min_x = min(min_x, newx)
            max_x = max(max_x, newx)
            min_y = min(min_y, newy)
            max_y = max(max_y, newy)

        width = max_x - min_x + 1
        height = max_y - min_y + 1
        width, height = float(width), float(height)
        print(width, height, time)
        return width, height, float(min_x), float(min_y)

    def box_area(self, time):
        width, height, *rest = self.box_dimension(time)
        return width * height


my_points = []
for i, _ in enumerate(xdata):
     my_points.append(TwoDPoint(xdata[i], ydata[i], dxdata[i], dydata[i]))

my_plot = MyPlot(set(my_points))


result = minimize(my_plot.box_area, 1)
seconds = int(round(result.x[0]))
width, height, min_x, min_y = my_plot.box_dimension(seconds)

# text = [['.'] * width for _ in range(height)]
# for x, y, vx, vy in points:
#     i = x + seconds * vx - min_x
#     j = y + seconds * vy - min_y
#     text[j][i] = '#'

# for line in text:
#     print(''.join(line))
# print(seconds)
