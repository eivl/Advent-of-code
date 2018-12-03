register = {}
highest_value = []
with open('input-day8.txt')as f:
    read_data = f.readlines()

read_data = [x.strip().split() for x in read_data]

for x in read_data:
    register[x[0]] = 0

for op in read_data:
    if op[0] in register:
        s = 'register["{}"] {} {}'.format(op[4], op[5], op[6])
        if eval(s):
            if op[1] == 'inc':
                register[op[0]] = register[op[0]] + int(op[2])
            else:
                register[op[0]] = register[op[0]] - int(op[2])
    else:
        if op[1] == 'inc':
            register[op[0]] = int(op[2])
        else:
            register[op[0]] = int(op[2])*-1
    highest_value.append(max(register.values()))
