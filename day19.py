from timeit import default_timer as timer

start = timer()

def addr(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] + result[b]
    return result

def addi(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] + b
    return result

def mulr(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] * result[b]
    return result

def muli(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] * b
    return result

def banr(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] & result[b]
    return result

def bani(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] & b
    return result

def borr(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] | result[b]
    return result

def bori(registers, a, b, c):
    result = registers[:]
    result[c] = result[a] | b
    return result

def setr(registers, a, b, c):
    result = registers[:]
    result[c] = result[a]
    return result

def seti(registers, a, b, c):
    result = registers[:]
    result[c] = a
    return result

def gtir(registers, a, b, c):
    result = registers[:]
    result[c] = bool(a > result[b])
    return result

def gtri(registers, a, b, c):
    result = registers[:]
    result[c] = bool(result[a] > b)
    return result

def gtrr(registers, a, b, c):
    result = registers[:]
    result[c] = bool(result[a] > result[b])
    return result

def eqir(registers, a, b, c):
    result = registers[:]
    result[c] = bool(a == result[b])
    return result

def eqri(registers, a, b, c):
    result = registers[:]
    result[c] = bool(result[a] == b)
    return result

def eqrr(registers, a, b, c):
    result = registers[:]
    result[c] = bool(result[a] == result[b])
    return result

registers = [0, 0, 0, 0, 0, 0]

with open('day19_input.txt') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]

ip = int(content[0].split()[1])
content.pop(0)

while True:
    try:
        op, a, b, c = content[registers[ip]].split()
    except IndexError as e:
        end = timer()
        print('Part 1: ', registers[0])
        break
    else:
        pass
    finally:
        pass
    registers = eval(op)(registers, int(a), int(b), int(c))
    registers[ip] += 1

print(end-start)
start = timer()


def fast(register_range):
    result = 0
    for i in range(1, register_range + 1):
        if register_range % i == 0:
            result += i
    print('Part 2:', result)

registers = [1, 0, 0, 0, 0, 0]
prev = 0
counter = 0
while True:
    try:
        op, a, b, c = content[registers[ip]].split()
    except IndexError as e:
        print(registers[0])
        break
    else:
        pass
    finally:
        pass
    registers = eval(op)(registers, int(a), int(b), int(c))
    registers[ip] += 1
    _next = registers[4]
    counter += 1
    if counter > 20: # start point after a few iterations
        if prev == _next:
            end = timer()
            fast(prev)
            break
        else:
            prev = _next

print(end-start)





# ip flow -> read value, run instruction, write value, increas by one

# ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
# ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
# ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
# ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
# ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]


# addi 2 16 2
# seti 1 1 1
# seti 1 4 3
# mulr 1 3 5
# eqrr 5 4 5
# addr 5 2 2
