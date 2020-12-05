"""Solver for Day 4, Problem 1 of Advent of Code 2020."""


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


def is_valid(passport_dict):
    """Make sure all required fields are present.

    Passport Fields:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """
    # NOTE: ``cid`` is optional.
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for field in required_fields:
        if field not in passport_dict:
            return False
    return True


def solve_it():
    """Solve https://adventofcode.com/2020/day/3 puzzle."""
    stripped_lines = load_stripped_passport_data()
    passports = parse_passports(stripped_lines)
    valid_count = sum(1 for p in passports if is_valid(p))
    print(f"{valid_count} valid passports.")


if __name__ == "__main__":
    solve_it()
