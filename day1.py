from itertools import tee

with open('day1_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

print(sum(1 for a, b in pairwise(result) if b > a))

def threewise(iterable):
    for idx, num in enumerate(result):
        total = result[idx:idx+3]
        if len(total) != 3:
            break
        yield total


print(sum([1 for a, b in pairwise(threewise(result)) if sum(b) > sum(a)]))
