from itertools import tee

with open('day1_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

count = 0
for a, b in pairwise(result):
    if b > a:
        count += 1

print(count)

def threewise(iterable):
    for idx, num in enumerate(result):
        total = result[idx:idx+3]
        if len(total) != 3:
            break
        yield total

count = 0
for a, b in pairwise(threewise(result)):
    if sum(b) > sum(a):
        count += 1
print(count)