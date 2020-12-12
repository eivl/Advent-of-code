from itertools import tee
from collections import Counter
from functools import lru_cache


with open('day10_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

result.append(0)
result.sort()
result.append(max(result)+3)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

diff = [b-a for a, b in pairwise(result)]
c = Counter(diff)
print(c[1]*c[3])

@lru_cache
def count(i=0):
    if i == len(result) - 1:
        return True
    temp = []
    for n in range(1, len(result) - i):
        if result[n + i] - result[i] <= 3:
            temp.append(count(i + n))
    return sum(temp)

print(count())
