from collections import Counter


with open('day2_input.txt') as f:
    result = f.readlines()

data = [
        [
         list(map(int, part.split('-'))) if '-' in part
         else part.split(':')[0]
         for part in line.split()
        ]
        for line in result
       ]  # [[1, 4], 'm', 'mrfmmbjxr']


count = 0
for line in data:
    low, high, char, password = *line[0], *line[1:]
    counter = Counter(password)
    if low <= counter[char] <= high:
        count += 1

print(count)

count = 0
for line in data:
    low, high, char, password = *line[0], *line[1:]
    if char == password[low-1] or password[high-1] == char:
        if password[low-1] == password[high-1]:
            continue
        count += 1

print(count)
