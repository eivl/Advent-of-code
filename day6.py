from functools import wraps
from time import perf_counter as time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time() - start
            print(f"Exe-time of {func.__name__}: {end_ if end_ > 0 else 0} "
                  f"sec")
    return _time_it


with open('day6_input.txt') as f:
    result, *_ = f.read().splitlines()


class LanternFish:
    spawns = []

    def __init__(self, cycle=9):
        self.cycle = cycle
        LanternFish.spawns.append(self)

    def __repr__(self):
        return f'{self.cycle}'

    def day(self):
        if self.cycle == 0:
            self.cycle = 7
            LanternFish()
        self.cycle -= 1


for num in [int(num) for num in result.split(',')]:
    LanternFish(num)


for day in range(80):
    for fish in LanternFish.spawns:
        fish.day()
print(len(LanternFish.spawns))

fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for spawncycle in [int(num) for num in result.split(',')]:
    fish[spawncycle] += 1

@measure
def number_of_fish(n):
    fishes = fish.copy()
    for i in range(n):
        fishes[(i+7) % 9] += fishes[i%9]
    return sum(fishes)


print(number_of_fish(80))
print(number_of_fish(256))
