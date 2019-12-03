with open('day1_input.txt') as f:
    result = f.readlines()
result = [int(line.strip()) for line in result]

sum_part1 = sum((num//3)-2 for num in result)
print(sum_part1)


def ff(f):
    if (f//3)-2 < 0:
        return 0
    return f//3-2 + ff(f//3-2)

sum_part2 = sum(ff(num) for num in result)
print(sum_part2)
