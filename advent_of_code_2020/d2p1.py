"""Solver for Day 2, Problem 1 of Advent of Code 2020."""
import re
from collections import Counter


RULE_PARSER = re.compile(r"(?P<mini>\d+)-(?P<maxi>\d+) (?P<letter>[a-z])")


def load_data():
    """Load the data from the DB file."""
    with open("password-db.txt") as f:
        rules_and_passwords = (x.split(":") for x in f.readlines())
    return rules_and_passwords


def is_password_valid(password, rule):
    """Determine if password complies with rule."""
    m = RULE_PARSER.match(rule)
    minimum = int(m.group('mini'))
    maximum = int(m.group('maxi'))
    letter = m.group('letter')
    c = Counter(password)
    return minimum <= c[letter] <= maximum


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
