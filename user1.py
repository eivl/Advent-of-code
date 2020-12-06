import math

file = open("day4_input.txt")

ids = []

min = 0
max = 127
row = 0

ID = 0

minS = 0
maxS = 7
seat = 0

for line in file:
    for letter in line[0:7:1]:
        if letter == "F":
            max = math.ceil(max - ((max - min)/2))
        else:
            min = math.ceil(max - ((max - min)/2))
    if letter == "F":
        row = min
    else:
        row = max
    min = 0
    max = 127

    for letter in line[7:]:
        if letter == "L":
            maxS = math.ceil(maxS - ((maxS - minS)/2))
        else:
            minS = math.ceil(maxS - ((maxS - minS)/2))
    if letter == "L":
        seat = minS
    else:
        seat = maxS
    minS = 0
    maxS = 7

    ID = (row*8) + seat

    print ("Row: " + str(row) + " Col: " + str(seat) + " ID: " + str(ID))
    ids.append(ID)
ids.sort()
print(len(ids))
