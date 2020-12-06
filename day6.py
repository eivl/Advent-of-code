with open('day6_input.txt') as f:
    result = f.read().split('\n\n')

print(sum([len(set(''.join(ans.split()))) for ans in result]))

data = [[set(ans) for ans in chunk.split()] for chunk in result]
print(sum([len(ans) for ans in map(lambda a: set.intersection(*a), data)]))

