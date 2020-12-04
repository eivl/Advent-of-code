with open('day4_input.txt') as f:
    result = f.readlines()
result = [line.strip() for line in result]

test_ = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

print(result)
check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
temp = []
inner = []
count = 0
for items in result:
    if items:
        inner.extend(items.split())
        continue
    my_dict = dict(item.split(':') for item in inner)
    if all(c in my_dict for c in check):
        byr = int(my_dict['byr'])
        if not 1920 <= byr <= 2020:
            continue
        iyr = int(my_dict['iyr'])
        if not 2010 <= iyr <= 2020:
            continue
        eyr = int(my_dict['eyr'])
        if not 2020 <= eyr <= 2030:
            continue
        if 'in' in my_dict['hgt']:
            h = int(my_dict['hgt'][:-2])
            if not 59 <= h <= 76:
                continue
        elif 'cm' in my_dict['hgt']:
            h = int(my_dict['hgt'][:-2])
            if not 150 <= h <= 193:
                continue
        else:
            continue
        if '#' not in my_dict['hcl']:
            continue # feil?
        if not my_dict['ecl'] in 'amb blu brn gry grn hzl oth'.split():
            continue
        if not len(my_dict['pid']) == 9:
            continue
        count += 1
    inner = []

print(count)