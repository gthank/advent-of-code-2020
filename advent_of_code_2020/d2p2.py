"""Solver for Day 2, Problem 2 of Advent of Code 2020."""
import re


RULE_PARSER = re.compile(r"(?P<pos1>\d+)-(?P<pos2>\d+) (?P<letter>[a-z])")


def load_data():
    """Load the data from the DB file."""
    with open("password-db.txt") as f:
        rules_and_passwords = (x.split(":") for x in f.readlines())
    return rules_and_passwords


def is_password_valid(password, rule):
    """Determine if password complies with rule."""
    password = password.lstrip()
    m = RULE_PARSER.match(rule)
    pos1 = int(m.group('pos1'))
    pos2 = int(m.group('pos2'))
    letter = m.group('letter')
    # Account for 0-indexed vs 1-indexed.
    first = password[pos1 - 1]
    second = password[pos2 - 1]
    is_valid = first != second and (first == letter or second == letter)
    return is_valid


def solve_it():
    """Solve https://adventofcode.com/2020/day/2 puzzle."""
    rules_and_passwords = load_data()
    valid_passwords = [
        passwd
        for rule, passwd in rules_and_passwords
        if is_password_valid(passwd, rule)
    ]
    print(f"{len(valid_passwords)} valid passwords.")


if __name__ == "__main__":
    solve_it()
