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
        first = numbers[0]
        last = numbers[-1]
        result = int(first + last)
        total.append(result)
    return total


assert sum(calibration_value(example)) == 142

