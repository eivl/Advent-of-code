from itertools import tee

with open('day1_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


print(sum(b > a for a, b in pairwise(result)))


def threewise(iterable):
    for idx, num in enumerate(result):
        total = result[idx:idx+3]
        if len(total) != 3:
            break
        yield total


print(sum([sum(b) > sum(a) for a, b in pairwise(threewise(result))]))

'''salt-die
def compare(n):
    return sum(x < y for x, y in zip(DATA, DATA[n:]))

def part_one():
    return compare(1)

def part_two():
    return compare(3)
'''