from array import array
import itertools

with open('day12_input.txt') as f:
    content = f.readlines()

def binary_to_string(array):
    return ''.join(['#' if x else '.' for x in array])


PADDING = 5
RULE_LENGHT = 5
generations = 115

initial_state = content.pop(0).split()[2]
initial_state = '.'*PADDING + initial_state + '.'*PADDING # added padding, thanks Sedsarq
binary_state = array('b', [1 if x == '#' else 0 for x in initial_state])
content.pop(0)


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


def calculate_generation(array, gen):
    '''
    generates a binary array based on the grow_rules
    '''
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
    '''
    sums up a binary array that has 5 zeroes as padding
    '''
    return sum([i if x else 0 for i, x in enumerate(array, start=-5)])


def get_indexs(array):
    '''
    returns a list of indexes for the elements in the array
    used to manually find a stable increasing generation as a baseline
    '''
    index_list = []
    for i, n in enumerate(array):
        if n:
            index_list.append(i)
    return index_list


print(sum_binary_array(calculate_generation(binary_state, 20)))

crazy_gen = 50_000_000_000
# at generation 130 the plants have stabilized and now you just have to offset the indexes.. a programatic solution is to come later.
baseline = 130
stable_indexes = [100, 105, 111, 118, 123, 128, 134, 142, 150, 158, 163, 168, 173, 181, 189, 198, 208, 213, 219, 227]
print(sum([i+(crazy_gen-baseline) for i in stable_indexes]) - 100)

def find_stable_solution(array, confidence=10):
    '''
    Find
    '''
    running_stability_score = 0
    prev = 0
    for i in itertools.count():
        my_array = calculate_generation(array, i)
        my_indexes = get_indexs(my_array)
        relative_sum = sum(my_indexes)-(sum(my_array)*i)
        if i == 0:
            prev = sum(my_indexes)-(sum(my_array)*i)
            continue
        if relative_sum == prev:
            running_stability_score +=1
        else:
            running_stability_score = 0
            prev = relative_sum
        if running_stability_score == confidence:
            break
        if i == 1000:
            print('WTF, check code')
            i = None
            break
    if i:
        return i, my_indexes

baseline, stable_indexes = find_stable_solution(binary_state)
print(sum([i+(crazy_gen-baseline) for i in stable_indexes]) - (len(stable_indexes)*PADDING))
