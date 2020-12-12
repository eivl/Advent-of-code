startnum= int(input("Write a number that is less than or equal to 10: "))

total = 0
while startnum <=10:
    n = startnum**2
    print(n)
    total += n
    startnum = startnum + 1
print('───')
print(total)
print('═══')