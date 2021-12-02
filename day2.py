with open('day2_input.txt') as f:
    result = f.readlines()
result = [line.strip().split() for line in result]


pos = 0j
for direction, n in result:
    n = int(n)
    if direction == 'forward':
        pos += n
    elif direction == 'down':
        pos += n*1j
    elif direction == 'up':
        pos -= n*1j

print(int(pos.real * pos.imag))


pos = 0j
aim = 0
for direction, n in result:
    n = int(n)
    if direction == 'forward':
        pos += n + aim*n*1j
    elif direction == 'down':
        aim += n
    elif direction == 'up':
        aim -= n

print(int(pos.real * pos.imag))

