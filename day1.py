import heapq


with open('day1_input.txt') as f:
    result = f.read().split('\n\n')

sums = [sum(int(num) for num in group.split()) for group in result]

print(f'Part1:\t{max(sums)}')
print(f'Part2:\t{sum(heapq.nlargest(3, sums))}')