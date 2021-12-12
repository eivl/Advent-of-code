import networkx as nx


data = '''KF-sr
OO-vy
start-FP
FP-end
vy-mi
vy-KF
vy-na
start-sr
FP-lh
sr-FP
na-FP
end-KF
na-mi
lh-KF
end-lh
na-start
wp-KF
mi-KF
vy-sr
vy-lh
sr-mi'''


cave = nx.Graph(line.split('-') for line in data.splitlines())


def calculate_paths(node, seen=None, visit_again=False):
    if node == "end":
        return True

    if not seen:
        seen = set()

    if node.islower():
        if node not in seen:
            seen = seen | {node}
        elif not visit_again:
            visit_again = True

    return sum(calculate_paths(next_node, seen, visit_again) for next_node in
               cave[node] if next_node != "start"
               if next_node not in seen or not visit_again
               )


print(calculate_paths("start", visit_again=True))
print(calculate_paths("start"))
