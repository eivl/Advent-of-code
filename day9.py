from aoc_helper import measure
from math import prod
import networkx as nx

# heightmap = '''2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678'''.splitlines()

with open('day9_input.txt') as f:
    heightmap = f.read().splitlines()


def generate_graph():
    graph_row = len(heightmap[0])
    graph_column = len(heightmap)
    graph = nx.grid_graph((graph_row, graph_column))
    for row_idx, row in enumerate(heightmap):
        for col_idx, num in enumerate(row):
            graph.add_node((row_idx, col_idx), value=int(num))
    return graph


def height(node):
    return graph.nodes[node]['value']


graph = generate_graph()

@measure
def part1():
    return sum(height(i) + 1 for i in graph
               if all(height(i) < height(j) for j in graph[i]))


@measure
def part2():
    graph.remove_nodes_from([n for n in graph if height(n) == 9])
    return prod([len(c) for c in sorted(nx.connected_components(graph),
                                        key=len,
                                        reverse=True)][:3])


print(part1())
print(part2())
