import networkx
from timeit import default_timer as timer

start = timer()

with open('day20_input.txt') as f:
    content = f.read().strip('\n')

my_map = networkx.Graph()
my_stack = []
start = 0
position = 0


for char in content:
    if char in 'NESW':
        # Thanks for the imaginary axis suggestion alca
        walk = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[char]
        my_map.add_edge(position, position + walk)
        position += walk
    elif char == '|':
        position = start
    elif char == '(':
        my_stack.append(start)
        start = position
    elif char == ')':
        start = my_stack.pop()
paths = networkx.algorithms.shortest_path_length(my_map, 0)

end = timer()
part1 = max(paths.values())
part2 = sum(s >= 1000 for s in paths.values())
print(part1)
print(part2)
print(end-start)

