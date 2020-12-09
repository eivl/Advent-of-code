import re


with open('day7_input.txt') as f:
    raw = f.read()


def count(bag):
    return 1 + sum(n * count(inner) for inner, n in formulas[bag].items())

def part_one():
    return sum(map(has_shiny, formulas))

def part_two():
    return count("shiny gold") - 1  # -1 since we don't count the shiny gold bag itself!

def parse_raw():
    bags = re.findall(r"([a-z]+ [a-z]+) bags contain (.+)", raw)
    formula = re.compile(r"(\d+) ([a-z]+ [a-z]+) bag")
    return {bag: {inner: int(n) for n, inner in formula.findall(contents)} for bag, contents in bags}

formulas = parse_raw()

def has_shiny(bag):
    return "shiny gold" in formulas[bag] or any(map(has_shiny, formulas[bag]))

print(part_one())
print(part_two())
