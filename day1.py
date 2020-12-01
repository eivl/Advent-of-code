from itertools import combinations


with open('day1_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

for num in result:
    if 2020 - num in result:
        print(num*(2020-num))
        break


for num_a, num_b, num_c in combinations(result, 3):
    if num_a + num_b + num_c == 2020:
        print(num_a*num_b*num_c)
        break
