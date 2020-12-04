import dataclasses
from functools import partial


def validate_year(year, lower, upper):
    """Validate if the passport has a valid year."""
    return len(year) == 4 and (lower <= int(year) <= upper)


def validate_height(height):
    """
    Validate if the passport has valid height.
    cm and in are valid units.
    """
    if 'in' in height:
        return 59 <= int(height[:-2]) <= 76
    elif 'cm' in height:
        return 150 <= int(height[:-2]) <= 193
    else:
        return False


def validate_hair_colour(hair_colour):
    """Validate if the passport has correct colour 'hex' or not."""
    return False if (hair_colour[0] != '#' or len(hair_colour) != 7) else True


def validate_eye_colour(eye_colour):
    """Validate if the passport has a valid eye colour."""
    return eye_colour in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_passport_id(pid):
    """Validate if the passport has a valid id number."""
    return pid.isdigit() and len(pid) == 9


VALID_FIELDS = {
    'byr': partial(validate_year, lower=1920, upper=2002),
    'iyr': partial(validate_year, lower=2010, upper=2020),
    'eyr': partial(validate_year, lower=2020, upper=2030),
    'hgt': validate_height,
    'hcl': validate_hair_colour,
    'ecl': validate_eye_colour,
    'pid': validate_passport_id,
}


@dataclasses.dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None
    _valid_fields: bool = dataclasses.field(init=False)
    _valid_data: bool = dataclasses.field(init=False)


    @classmethod
    def create_from_raw_string(cls, string):
        """Create a Passport from a raw string"""
        passport = dict(item.split(':') for item in string.split())
        return cls(**passport)

    def __post_init__(self):
        """Validate passports"""
        self._valid_fields = all(getattr(self, field) for field in VALID_FIELDS)
        validate_fields = (func(getattr(self, field)) for field, func in
                           VALID_FIELDS.items())
        self._valid_data = self._valid_fields and all(validate_fields)


    @property
    def valid_fields(self):
        """Check if the passport has valid fields"""
        return self._valid_fields

    @property
    def is_valid(self):
        """Check if the passport had valid data"""
        return self._valid_data


def part_a(puzzle_input):
    """Return the answer for part A."""
    data = [Passport.create_from_raw_string(raw_string)
            for raw_string in puzzle_input.split('\n\n')]
    return sum(passport.valid_fields for passport in data)


def part_b(puzzle_input):
    """Return the answer for part B."""
    data = [Passport.create_from_raw_string(raw_string)
            for raw_string in puzzle_input.split('\n\n')]
    return sum(passport.is_valid for passport in data)


with open('day4_input.txt') as f:
    result = f.read()

print(part_a(result))
print(part_b(result))

