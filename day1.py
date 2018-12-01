with open('day1_input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
score = sum(content)
print(score)

# Part 2
import itertools

input_cycle = itertools.cycle(content)
running_score = 0
seen_frequencies = set()
for n in input_cycle:
    running_score += n
    if running_score in seen_frequencies:
        break
    else:
        seen_frequencies.add(running_score)
    # Debuging :D
#    if len(seen_frequencies) % 1_000 == 0:
#        print(running_score)
print(running_score)
