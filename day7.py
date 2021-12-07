from statistics import mean, median

from aoc_helper import measure

with open('day7_input.txt') as f:
    result = [int(num) for num in f.read().split(',')]

# result = [16,1,2,0,4,2,7,1,2,14]


def get_fuel(pos, target):
    return sum(range(1, abs(pos-target)+1))


@measure
def solution():
    guess = int(mean(result))
    fuel = []
    for i in range(int(median(result)), int(median(result)+1)):
        fuel.append(sum(abs(n - i) for n in result))

    fuel_ext = []
    for i in range(guess-1, guess+2):
        fuel_ext.append(sum(get_fuel(n, i) for n in result))

    return fuel[0] + min(fuel_ext)*1j


print(solution())
