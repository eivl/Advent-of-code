from operator import itemgetter

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

# Part 2
example = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

NUMBER_MAPPING = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def fix_calibration_string(string):
    '''
    eightwothree -> 8wo3
    '''
    result = []
    for line in string.splitlines():
        replace_mapping = {}

        for key in NUMBER_MAPPING:
            if key in line:
                replace_mapping[key] = line.find(key)

        sorted_mapping = sorted(replace_mapping.items(), key=itemgetter(1))

        for key, value in sorted_mapping:
            line = line.replace(key, NUMBER_MAPPING[key])

        result.append(line)
    string = '\n'.join(result)
    return string


assert fix_calibration_string('eightwothree') == '8wo3'
real_example = fix_calibration_string(example)
assert sum(calibration_value(real_example)) == 281

real_input = fix_calibration_string(content)
print(sum(calibration_value(real_input)))
