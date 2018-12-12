from array import array

with open('day12_input.txt') as f:
    content = f.readlines()

def binary_to_string(array):
    return ''.join(['#' if x else '.' for x in array])


initial_state = content.pop(0).split()[2]
initial_state = '.....' + initial_state + '.....' # added padding, thanks Sedsarq
binary_state = array('b', [1 if x == '#' else 0 for x in initial_state])

content.pop(0)

RULE_LENGHT = 5
generations = 115

grow_rules = []
die_rules = []
for line in content:
    rules = line.split()[0]
    if line.rsplit()[-1] == '#':
        grow_rules.append(array('b', [1 if x == '#' else 0 for x in rules]))
    elif line.rsplit()[-1] == '.':
        die_rules.append(array('b', [1 if x == '#' else 0 for x in rules]))
    else:
        print('Something strange going on: ', line)

backup = binary_state[:]


for gen in range(generations):
    bstate_copy = binary_state[:]
    for i, b in enumerate(binary_state):
        if binary_state[i:RULE_LENGHT+i] in grow_rules:
            bstate_copy[i+2] = 1
        else:
            try:
                bstate_copy[i+2] = 0
            except IndexError:
                pass
    binary_state = bstate_copy[:]
    if sum(binary_state[-5:]) > 0:
        binary_state.insert(len(binary_state), 0)
    if gen == 19:
        print(sum([i if x else 0 for i, x in enumerate(binary_state, start=-5)]))


def calculate_generation(array, gen):
    for gen in range(gen):
        bin_state_copy = array[:]
        for i, b in enumerate(array):
            if array[i:RULE_LENGHT+i] in grow_rules:
                bin_state_copy[i+2] = 1
            else:
                try:
                    bin_state_copy[i+2] = 0
                except IndexError:
                    pass
        array = bin_state_copy[:]
        if sum(array[-5:]) > 0:
            array.insert(len(array), 0)
    return array

def sum_binary_array(array):
    return sum([i if x else 0 for i, x in enumerate(array, start=-5)])


def get_first_index(array):
    index_list = []
    for i, n in enumerate(array):
        if n:
            index_list.append(i)
    return index_list

my_sum = sum(get_first_index(calculate_generation(backup, 130))) -(20*5)


crazy_gen = 50_000_000_000
# at generation 130 the plants have stabilized and now you just have to offset the indexes.. a programatic solution is to come later.
baseline = 130
indexes = [100, 105, 111, 118, 123, 128, 134, 142, 150, 158, 163, 168, 173, 181, 189, 198, 208, 213, 219, 227]
first_attempt = []
for i in indexes:
    first_attempt.append(i+(crazy_gen-baseline))

print(sum(first_attempt)-100)
