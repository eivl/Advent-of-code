import heapq


with open('day1_input.txt') as f:
    result = f.read().split('\n\n')

sums = [sum(int(number) for number in calories.split()) for calories in result]
print(f'Part1:\t{max(sums)}')
print(f'Part2:\t{sum(heapq.nlargest(3, sums))}')
