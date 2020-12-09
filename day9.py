from itertools import combinations



with open('day9_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]
preamble, result = result[:25], result[25:]


check = [sum(n) for n in (combinations(preamble, 2))]
for i, n in enumerate(result):
    if n not in check:
        part_one = n
        print('index:', i, 'value:', n)  # 776203571
        break
    preamble.append(n)
    check = [sum(n) for n in (combinations(preamble, 2))]


def all_sub_lists(sub_list):
    n = len(sub_list)
    indices = list(range(n+1))
    for i, j in combinations(indices, 2):
        if j - i == 1:
            continue
        yield sub_list[i:j]

for sub_list in all_sub_lists(result):
    if sum(sub_list) == part_one:
        print(min(sub_list) + max(sub_list))