# from itertools import cycle
day10 = """
34, 88, 2, 222, 254, 93, 150, 0, 199, 255, 39, 32, 137, 136, 1, 167
""".strip()

test = """
1,2,4
""".strip()


def part1(seq):
    length = 256
    pos = 0
    skip = 0
    start = list(range(length))
    seq = list(map(int, seq.split(',')))
    for ln in seq:
        back = max(0, pos - length)
        back2 = max(0, pos + ln - length)
        st = start[pos: pos + ln] + start[back: back2]
        st = st[::-1]

        top = length - pos

        start[pos: pos + ln] = st[:top]
        start[back: back2] = st[top:]

        pos += ln + skip
        skip += 1
        pos %= length

    print(start[0] * start[1])


def part2(seq):
    length = 256
    pos = 0
    skip = 0
    start = list(range(length))
    seq = list(map(ord, seq))
    seq += [17, 31, 73, 47, 23]
    for _ in range(64):
        for ln in seq:
            back = max(0, pos - length)
            back2 = max(0, pos + ln - length)
            st = start[pos: pos + ln] + start[back: back2]
            st = st[::-1]

            top = length - pos
            start[pos: pos + ln] = st[:top]
            start[back: back2] = st[top:]

            pos += ln + skip
            skip += 1
            pos %= length

    agg = []

    for i in range(0, 256, 16):
        a = 0
        for c in start[i: i + 16]:
            a ^= c
        agg.append(a)
    print(''.join(f'{a:x}' for a in agg))


part2(test)
