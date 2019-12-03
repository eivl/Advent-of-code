data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]

def add(a, b):
    return a+b

def mul(a, b):
    return a*b

op_codes = {
    1: add,
    2: mul
}

def cal_addresse(data, noun=12, verb=2):
    data[1] = noun
    data[2] = verb
    for i in range(0, len(data), 4):
        opc, a, b , z = data[i:i+4]
        if opc == 99:
            break
        data[z] = op_codes[opc](data[a], data[b])
    return data[0]

print(cal_addresse(data[:]))
magic_number = 19690720
for noun in range(100):
    for verb in range(100):
        result = cal_addresse(data[:], noun, verb)
        if result == magic_number:
            print(noun*100+verb)
