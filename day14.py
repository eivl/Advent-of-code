from timeit import default_timer as timer
start = timer()
puzzle_input = 580741

def list_from_number(n):
    '''
    return list of numbers
    '''
    return [int(d) for d in str(n)]

def number_from_list(lst):
    return int(''.join(map(str, lst)))

def sum_digits(n):
    result = 0
    while n:
        result, n = result + n % 10, n // 10
    return result

elf1 = 0
elf2 = 1

scoreboard = [3,7]
seq = list_from_number(puzzle_input)

for _ in range(puzzle_input*36): # estimating the size
    current_score = scoreboard[elf1] + scoreboard[elf2]
    if current_score < 10:
        scoreboard.append(current_score)
    else:
        scoreboard.append(1)
        scoreboard.append(list_from_number(current_score)[1])
    elf1 = (elf1 + (scoreboard[elf1] + 1))%len(scoreboard)
    elf2 = (elf2 + (scoreboard[elf2] + 1))%len(scoreboard)
    if elf1 == elf2:
        elf2 += 1
    if seq == scoreboard[-5:]: # does not work
        print(scoreboard[-5:])
        break


indexes = []

for i in range(len(scoreboard)):
    if seq == scoreboard[i:i+6]:
        print(i)
        break
end=timer()
print(end-start)
