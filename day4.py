from collections import defaultdict
import operator

with open('day4_input.txt') as f:
    content = f.readlines()

guard_id = 0
guards = defaultdict(int)
max_sleep = defaultdict(lambda: defaultdict(int))

for line in sorted(content):
    line_data = line.split()
    # get Guard ID and time
    if line_data[3].startswith('#'):
        guard_id = int(line_data[3][1:])
        wake_up = int(line_data[1].split(':')[1][:2])
    # get sleep time
    if 'falls asleep' in line:
        sleep = int(line.split(':')[1][:2])
    # get wake time and duration, generate sleep dict
    if 'wakes up' in line:
        wake_up = int(line.split(':')[1][:2])
        duration = wake_up - sleep
        guards[guard_id] += duration
        for i in range(sleep, wake_up):
            max_sleep[guard_id][i] += 1

chosen_id = max(guards.items(), key=operator.itemgetter(1))[0]
chosen_min = max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0]

result = chosen_id * chosen_min
print(result)

#part2

maximum_guards_asleep = 0
for guard_id, element in max_sleep.items():
    current_max = max(element.items(), key=operator.itemgetter(1))[1]
    if current_max > maximum_guards_asleep:
        chosen_id = guard_id
        maximum_guards_asleep = current_max
chosen_min = max(max_sleep[chosen_id].items(), key=operator.itemgetter(1))[0]
result = chosen_id * chosen_min
print(result)
