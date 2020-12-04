from pprint import pprint
import re

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('day4_input.txt') as f:
    result = f.read()



def is_valid(passport):
    return not any(required - passport.keys())


passports = []
for chunk in result.split('\n\n'):
    matches = re.findall(r'(\w+):(\S+)', chunk)
    passports.append({key: value for key, value in matches})

print(sum(map(is_valid, passports)))


def is_valid_b(passport):
    try:
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002:
            return False
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            return False
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            return False
        hgt = passport['hgt']
        match = re.match(r'(\d+)(cm|in)', hgt)
        height, unit = match[1], match[2]
        if unit == 'cm':
            if not 150 <= int(height) <= 193:
                return False
        elif unit == 'in':
            if not 59 <= int(height) <= 76:
                return False
        else:
            return False
        hcl = passport['hcl']
        if hcl[0] != '#' or len(hcl) != 7:
            return False
        ecl = passport['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        pid = passport['pid']
        if not pid.isdigit() or len(pid) != 9:
            return False
        return True
    except Exception:
        return False


print(sum(map(is_valid_b, passports)))
