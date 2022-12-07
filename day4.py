import re

with open('day4_input.txt') as f:
    result = f.read().splitlines()

test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

sums = []
for line in result:
    a, b, c, d = (int(num) for num in re.findall('[0-9]+', line))
    sums.append(a <= c and d <= b or c <= a and b <= d)

print(sum(sums))

sums = []
for line in result:
    a, b, c, d = (int(num) for num in re.findall('[0-9]+', line))
    check = a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d
    sums.append(check)

print(sum(sums))
