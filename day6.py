import collections
from itertools import islice


def sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solve(string, length=4):
    count = length
    for window in sliding_window(string, length):
        if len(set(window)) == length:
            return count
        else:
            count += 1


with open('day6_input.txt') as f:
    result = f.read()

print(solve(result))
print(solve(result, length=14))
