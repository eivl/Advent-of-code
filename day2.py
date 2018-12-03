from collections import Counter
import itertools
import difflib


with open('day2_input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

twos = []
threes = []

for line in content:
    c = Counter(line)
    rev = {v: k for k, v in c.items()}

    for key, value in rev.items():
        if key == 2:
            twos.append(key)
        elif key == 3:
            threes.append(key)

result = len(twos) * len(threes)
print(result)


similar_chars = []
different_chars = []

for combi in itertools.combinations(content, 2):
    for diff_string in difflib.ndiff(*combi):
        if diff_string[0]==' ':
            similar_chars.append(diff_string.strip())
        elif diff_string[0]=='-':
            different_chars.append(diff_string)
        if len(different_chars) > 1:
            similar_chars.clear()
            different_chars.clear()
            break
    if similar_chars:
        print(''.join(similar_chars))
        break
