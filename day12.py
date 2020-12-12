with open('day12_input.txt') as f:
    result = f.readlines()
result = [(line[0], int(line[1:].strip())) for line in result]

DIRECTION = {
    'N': 1j,
    'E': 1,
    'S': -1j,
    'W': -1,
    'L': -1,
    'R': 1
}

HEADING = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}



START_HEADING = 90
heading = START_HEADING
position = (0+0j)
waypoint = (10+1j)


def move(pos, direction, distance):
    return pos + DIRECTION[direction]*distance


def change_heading(head, direction, angle):
    head += DIRECTION[direction]*angle
    return head % 360


for direction, value in result:
    if direction in 'LR':
        heading = change_heading(heading, direction, value)
    elif direction in 'NESW':
        position = move(position, direction, value)
    elif direction == 'F':
        position = move(position, HEADING[heading], value)
    else:
        print('something is wrong', direction, value)

print(int(abs(position.real) + abs(position.imag)))


heading = START_HEADING
position = (0+0j)
waypoint = (10+1j)


def rotate_90(way, cw=1, turns=1):
    """Rotate 90 degrees clockwise or counterclockwise (-1)"""
    for _ in range(turns):
        way = complex(cw*way.conjugate().imag, cw*way.conjugate().real)
    return way

def move_to_way(pos, way, distance):
    return pos + way*distance


for direction, value in result:
    if direction in 'LR':
        waypoint = rotate_90(waypoint, -1*DIRECTION[direction], value//90)
    elif direction in 'NESW':
        waypoint = move(waypoint, direction, value)
    elif direction == 'F':
        position = move_to_way(position, waypoint, value)
    else:
        print('something is wrong', direction, value)

print(int(abs(position.real) + abs(position.imag)))
