with open('day1_input.txt') as f:
    content = f.readlines()
running_score = sum([int(x.strip()) for x in content])
print(running_score)
