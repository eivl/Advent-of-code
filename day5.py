from day5_input import DAY5_INPUT
import string
from timeit import default_timer as timer
from multiprocessing import Pool


start = timer()

def part1():
    stack = []
    for char in DAY5_INPUT:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] != char and stack[-1].lower() == char.lower():
            stack.pop()
        else:
            stack.append(char)
    return len(stack), stack
result, stack = part1()


end = timer()
print(result)
print(end - start)

def part2(DAY5_INPUT):
    shortest_poly = None
    for test_polymer in string.ascii_lowercase:

        modified_input = DAY5_INPUT.replace(test_polymer.upper(), '')
        modified_input = modified_input.replace(test_polymer, '')
        stack = []
        for char in modified_input:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
        stack_length = len(stack)
        if shortest_poly is None or shortest_poly > stack_length:
            shortest_poly = stack_length
    return shortest_poly


def part2_redone(test_polymer, DAY5_INPUT=DAY5_INPUT):
    shortest_poly = None
    modified_input = DAY5_INPUT.replace(test_polymer.upper(), '')
    modified_input = modified_input.replace(test_polymer, '')
    stack = []
    for char in modified_input:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] != char and stack[-1].lower() == char.lower():
            stack.pop()
        else:
            stack.append(char)
    stack_length = len(stack)
    if shortest_poly is None or shortest_poly > stack_length:
        shortest_poly = stack_length
    return shortest_poly

pool = Pool()
start = timer()
result = pool.map(part2_redone, string.ascii_lowercase)
end = timer()
pool.close()
pool.join()
print(min(result))
print(end - start)
