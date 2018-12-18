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

def string_to_list(string):
    try:
        result = eval(string)
    except SyntaxError:
        return None
    except NameError:
        return None
    else:
        if isinstance(result, list):
            return result
        else:
            print('not list')

OPCODES = (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, 
           gtir, gtri, gtrr, eqir, eqri, eqrr)

with open('day16_input.txt') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]

def calculate_instructions(instruction, before, after):
    result = set()
    for op in OPCODES:
        op_result = op(before, *instruction[1:])
        if op_result == after:
            result.add(op)
    return result



i = 0
exp = []
while True:
    before, instruction, after = content[i:i+3]
    i += 4
    exp.append((
        list(map(int, instruction.split(' '))),
        string_to_list(before[8:]),
        string_to_list(after[8:])
    ))
    if not content[i]:
        break

print(len([e for e in exp if len(calculate_instructions(*e)) >= 3]))
