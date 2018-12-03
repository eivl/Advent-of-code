from collections import Counter


with open('day2_input.txt') as f:
    content = f.readlines()

twos = []
threes = []

for line in content:
    c = Counter(line.strip())
    rev = {v: k for k, v in c.items()}

    for key, value in rev.items():
        if key == 2:
            twos.append(key)
        elif key == 3:
            threes.append(key)

result = len(twos) * len(threes)
print(result)
