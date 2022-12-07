from itertools import zip_longest
from string import ascii_letters


def grouper(iterable, n):
    return zip_longest(*[iter(iterable)] * n)


with open('day3_input.txt') as f:
    result = f.read().splitlines()


sums = []
for line in result:
    char, = set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))
    sums.append(ascii_letters.index(char)+1)
print(sum(sums))

sums = []
for l1, l2, l3 in grouper(result, 3):
    char, = set(l1).intersection(set(l2)).intersection(set(l3))
    sums.append(ascii_letters.index(char)+1)

print(sum(sums))
