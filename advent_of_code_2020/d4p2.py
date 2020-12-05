"""Solver for Day 4, Problem 2 of Advent of Code 2020."""
import re


HEX_COLOR_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")
PASSPORT_ID_PATTERN = re.compile(r"^[0-9]{9}$")


def load_stripped_passport_data():
    """Load the lines out of the passport batch file w/o trailing spaces."""
    stripped = []
    with open("passports.txt") as f:
        stripped = [line.strip() for line in f.readlines()]
    return stripped


def parse_passports(stripped_lines):
    """Iterate over ``stripped_lines`` and parse them into a list of dicts."""
    passports = []
    cur_passport = {}
    for line in stripped_lines:
        if line == "":
            passports.append(cur_passport)
            cur_passport = {}
            continue

        fields = line.split()
        for field in fields:
            key, value = field.split(":")
            cur_passport[key] = value
    if len(cur_passport) > 0:
        passports.append(cur_passport)
    return passports


def validate_byr(passport):
    """Validate Birth Year - four digits; at least 1920 and at most 2002."""
    byr = passport.get("byr", None)
    if byr is None:
        return False
    byr = int(byr)
    return 1920 <= byr <= 2002


def validate_iyr(passport):
    """Validate issue year - four digits; at least 2010 and at most 2020."""
    iyr = passport.get("iyr", None)
    if iyr is None:
        return False
    iyr = int(iyr)
    return 2010 <= iyr <= 2020


def validate_eyr(passport):
    """Validate expiration year - four digits; >= 2020 and <= 2030."""
    eyr = passport.get("eyr", None)
    if eyr is None:
        return False
    eyr = int(eyr)
    return 2020 <= eyr <= 2030


def validate_hgt(passport):
    """Validate height - a number followed by either cm or in.

    * If cm, the number must be at least 150 and at most 193.
    * If in, the number must be at least 59 and at most 76.
    """
    hgt = passport.get("hgt", None)
    if hgt is None:
        return False
    unit = hgt[-2:]
    value = hgt[0:-2]
    if unit == "in":
        return 59 <= int(value) <= 76
    elif unit == "cm":
        return 150 <= int(value) <= 193

    return False


def validate_hcl(passport):
    """Validate hair color - a # followed by exactly six hex characters."""
    hcl = passport.get("hcl", "")
    return HEX_COLOR_PATTERN.match(hcl)


def validate_ecl(passport):
    """Validate eye color - exactly one of: amb blu brn gry grn hzl oth."""
    ecl = passport.get("ecl", None)
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(passport):
    """Validate Passport ID - a nine-digit number, including leading zeroes."""
    pid = passport.get("pid", "")
    return PASSPORT_ID_PATTERN.match(pid)


def is_valid(passport_dict):
    """Make sure all required fields are present and valid.

    Passport Fields:

    * byr (Birth Year)
    * iyr (Issue Year)
    * eyr (Expiration Year)
    * hgt (Height)
    * hcl (Hair Color)
    * ecl (Eye Color)
    * pid (Passport ID)
    * cid (Country ID)

    .. NOTE: ``cid`` is optional.
    """
    validators = (
        validate_byr,
        validate_iyr,
        validate_eyr,
        validate_hgt,
        validate_hcl,
        validate_ecl,
        validate_pid,
    )
    results = [v(passport_dict) for v in validators]
    return all(results)


def solve_it():
    """Solve https://adventofcode.com/2020/day/3 puzzle."""
    stripped_lines = load_stripped_passport_data()
    passports = parse_passports(stripped_lines)
    valid_count = sum(1 for p in passports if is_valid(p))
    print(f"{valid_count} valid passports.")


if __name__ == "__main__":
    solve_it()
