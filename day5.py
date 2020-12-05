with open('day5_input.txt') as f:
    result = f.readlines()
result = [line.strip() for line in result]

replacement = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}
binary_list = [
               ''.join([replacement.get(char, char) for char in line])
               for line in result
               ]


def seat_ids(passes, hash_factor=8):
    for b_pass in passes:
        yield int(b_pass[:-3], base=2) * hash_factor + int(b_pass[-3:], base=2)


print(f'Answer to part1: {max(seat_ids(binary_list))}')

taken = set(seat_ids(binary_list))
front = 61  # magic number to remove the front
back = 995  # magic number to remove the back
available = set(n for n in range(front, back))
print(f'Answer to part2: {available.difference(taken)}')


