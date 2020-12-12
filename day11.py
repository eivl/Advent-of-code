from collections import Counter


with open('day11_input.txt') as f:
    result = f.readlines()
room = [line.strip() for line in result]
ROW_LENGTH = len(room[0])
COLUMN_HEIGHT = len(room)

def padd_room(room):
    padded_room = ['.' + row + '.' for row in room]
    padded_room.insert(0, '.'*(ROW_LENGTH+2))
    padded_room.append('.'*(ROW_LENGTH+2))
    return padded_room


"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor
"""


def check_seat(pos=(0, 0)):
    x, y = pos
    padded_room = padd_room(room)
    count = how_many_adjacent(padded_room, pos=pos)


def how_many_adjacent(padded_room, pos=(0, 0)):
    adjacent = []
    x, y = pos
    x += 1
    y += 1
    adjacent.append(padded_room[x-1][y - 1:y + 2])
    adjacent.append(padded_room[x][y-1:y+2:2])
    adjacent.append(padded_room[x+1][y - 1:y + 2])
    count = Counter(''.join(adjacent))
    return count


def move_around():
    changes = []
    for x, row in enumerate(room):
        for y, seat in enumerate(row):
            count = how_many_adjacent(padd_room(room), pos=(x, y))
            if seat == 'L' and count['#'] == 0:
                yield '#'
            elif seat == '#' and count['#'] >= 4:
                yield 'L'
            else:
                yield seat


def next_set():
    l = []
    row = []
    for char in move_around():
        if len(row) % ROW_LENGTH == 0 and len(row) > 0:
            l.append(''.join(row[-ROW_LENGTH:]))
        row.append(char)
    l.append(''.join(row[-ROW_LENGTH:]))
    return l


def part_one():
    global room
    while True:
        previous_room, room = room, next_set()
        if room == previous_room:
            print('first example')
            previous_room, room = room, next_set()
            if room == previous_room:
                return Counter(''.join(room))['#']


# print(part_one())


with open('day11_input.txt') as f:
    result = f.readlines()
room = [line.strip() for line in result]


def find_nearest(pos):
    x, y = pos
    rotated = list(zip(*room))

    def _north():
        north = ''.join(rotated[y][:x][::-1])
        north = north.replace('.', '')
        return '.' if not north else north[0]

    def _north_east():
        nonlocal y
        j = y
        tmp = []
        for i in range(x, -1, -1):
            if j > len(room[i]):
                continue
            try:
                tmp.append(room[i][j])
            except:
                pass
            j += 1
        north_east = ''.join(tmp[1:]).replace('.', '')
        return '.' if not north_east else north_east[0]

    def _east():
        east = room[x][y + 1:]
        east = east.replace('.', '')
        return '.' if not east else east[0]

    def _south_east():
        nonlocal y
        j = y
        tmp = []
        for i in range(x, len(room)):
            if j > len(room[i]):
                continue
            try:
                tmp.append(room[i][j])
            except:
                pass
            j += 1
        south_east = ''.join(tmp[1:]).replace('.', '')
        return '.' if not south_east else south_east[0]

    def _south():
        south = ''.join(rotated[y][x + 1:])
        south = south.replace('.', '')
        return '.' if not south else south[0]

    def _south_west():
        nonlocal y
        j = y
        tmp = []
        for i in range(x, len(room)):
            if j < 0:
                continue
            tmp.append(room[i][j])
            j -= 1

        south_east = ''.join(tmp[1:]).replace('.', '')
        return '.' if not south_east else south_east[0]

    def _west():
        west = room[x][:y][::-1]
        west = west.replace('.', '')
        return '.' if not west else west[0]

    def _north_west():
        nonlocal y
        j = y
        tmp = []
        for i in range(x, 0, -1):
            if j < 0:
                continue
            tmp.append(room[i][j])
            j -= 1
        north_west = ''.join(tmp[1:]).replace('.', '')
        return '.' if not north_west else north_west[0]

    return [_north(), _north_east(), _east(), _south_east(), _south(), _south_west(), _west(), _north_west()]


def how_many_los(padded_room, pos=(0, 0)):
    adjacent_los = find_nearest(pos)
    count = Counter(''.join(adjacent_los))
    print(count)
    return count


def move_around_two():
    for x, row in enumerate(room):
        for y, seat in enumerate(row):
            count = how_many_los(padd_room(room), pos=(x, y))
            if seat == 'L' and count['#'] == 0:
                yield '#'
            elif seat == '#' and count['#'] >= 5:
                yield 'L'
            else:
                yield seat

def next_set_two():
    l = []
    row = []
    for char in move_around_two():
        if len(row) % ROW_LENGTH == 0 and len(row) > 0:
            l.append(''.join(row[-ROW_LENGTH:]))
        row.append(char)
    l.append(''.join(row[-ROW_LENGTH:]))
    return l


def part_two():
    global room
    while True:
        previous_room, room = room, next_set_two()
        if room == previous_room:
            print('second example')
            print(room)
            previous_room, room = room, next_set_two()
            if room == previous_room:
                return Counter(''.join(room))['#']

print(part_two())


