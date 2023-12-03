example = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''


def calibration_value(string):
    total = []
    for line in string.splitlines():
        numbers = [char for char in line if char.isdigit()]
        total.append(int(numbers[0] + numbers[-1]))
    return total


assert sum(calibration_value(example)) == 142

with open('day1_input.txt') as file:
    content = file.read()

result = calibration_value(content)
print(sum(result))
