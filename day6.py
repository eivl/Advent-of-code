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


def number_of_fish(n):
    fishes = fish.copy()
    for i in range(n):
        fishes[(i+7) % 9] += fishes[i%9]
    return sum(fishes)


print(number_of_fish(80))
print(number_of_fish(256))
