import copy

with open('day7_input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

graph = {}
order = []

for line in content:
    data = line.split()
    before, after = data[1], data[-3]
    if after not in graph:
        graph[after] = set()
    if before not in graph:
        graph[before] = set()
    graph[after].add(before)

worker_graph = copy.deepcopy(graph)
while True:
    selected = None
    for char in graph:
        if len(graph[char]) == 0 and (selected is None or selected > char):
            selected = char
    order.append(selected)
    del graph[selected]
    for char in graph:
        if selected in graph[char]:
            graph[char].remove(selected)
    if len(graph) == 0:
        break
print(''.join(order))


# part2
def selected_next(graph, done):
    for char in graph:
        if len(graph[char]) == 0 and char not in done:
            return char
    return None

workers = 5
time = 0
done = set()
time_to_add = 60 - ord('A') + 1  # same as 60 + string.ascii_uppercase.find()+1
next_workers = [None] * workers
worker_tasks = [None] * workers

while len(worker_graph) > 0:
    if not any(next_w is None or next_w == time for next_w in next_workers):
        time += 1
        continue
    while any(next_w == time for next_w in next_workers):
        index = next_workers.index(time)
        if worker_tasks[index] is not None:
            selected = worker_tasks[index]
            del worker_graph[selected]
            for char in worker_graph:
                if selected in worker_graph[char]:
                    worker_graph[char].remove(selected)
        selected = selected_next(worker_graph, done)

        if selected is None:
            next_workers[index] = None
            worker_tasks[index] = None
        else:
            done.add(selected)
            worker_tasks[index] = selected
            next_workers[index] = time + time_to_add + ord(selected)
    selected = selected_next(worker_graph, done)
    while selected is not None and any(next_w is None for next_w in next_workers):
        done.add(selected)
        index = next_workers.index(None)
        worker_tasks[index] = selected
        next_workers[index] = time + time_to_add + ord(selected)
        selected = selected_next(worker_graph, done)
    time += 1


print(time-1)
