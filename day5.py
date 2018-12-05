from day5_input import DAY5_INPUT
import string


def part1():
    stack = []
    for char in DAY5_INPUT:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] != char and stack[-1].lower() == char.lower():
            stack.pop()
        else:
            stack.append(char)
    return len(stack)
print(part1())

def part2():
    shortest_poly = None
    for test_polymer in string.ascii_lowercase:
        stack = []
        modified_input = DAY5_INPUT.replace(test_polymer.upper(), '')
        modified_input = modified_input.replace(test_polymer, '')

        for char in modified_input:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] != char and stack[-1].lower() == char.lower():
                stack.pop()
            else:
                stack.append(char)
        if shortest_poly is None or shortest_poly > len(stack):
            shortest_poly = len(stack)
            # print(shortest_poly, test_polymer)
        else:
            # print('->', len(stack), test_polymer)
            pass
    return shortest_poly

print(part2())
