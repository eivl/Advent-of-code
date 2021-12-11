with open('day11_input.txt') as f:
    result = f.read().splitlines()

octo = {}
for i, row in enumerate(result):
    for j, cell in enumerate(row):
        octo[complex(i, j)] = int(cell)


def neighbors(location):
    offsets = (1, 1j, -1, -1j, 1-1j, 1+1j, -1+1j, -1-1j)
    for diff in offsets:
        if octo.get(location+diff):
            yield location+diff


count = 0
for step in range(1000):
    for location in octo:
        octo[location] += 1

    max_energy = {location for location in octo if octo[location] > 9}
    while max_energy:
        location = max_energy.pop()
        octo[location] = 0
        for o in neighbors(location):
            octo[o] += 1
            if octo[o] > 9:
                max_energy.add(o)
    count += sum(octo[location] == 0 for location in octo)
    if step == 99:
        print(count)
    if not any(octo.values()):
        print(step+1)
        break
