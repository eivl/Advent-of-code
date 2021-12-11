from statistics import median

# data = '''[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]'''.splitlines()

with open('day10_input.txt') as f:
    data = f.read().splitlines()

MAP = {
    '[': ']',
    '(': ')',
    '<': '>',
    '{': '}',
}

SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

CLOSING = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def solution(part1=True):
    illegal = []
    broken_lines = []
    for line in data:
        flag = True
        opened = []
        for char in line:
            if char in MAP:
                opened.append(char)
            elif char in MAP.values():
                if MAP[opened[-1]] == char:
                    opened.pop()
                else:
                    illegal.append(SCORE[char])
                    flag = False
                    break
        if flag:
            score = 0
            for idx, char in enumerate(opened[::-1]):
                char = MAP[char]
                score = score*5 + CLOSING[char]
            broken_lines.append(score)

    if part1:
        print(sum(illegal))
    else:
        print(median(broken_lines))


solution()
solution(False)