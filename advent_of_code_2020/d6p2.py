"""Solver for Day 6, Problem 2 of Advent of Code 2020."""
import re


WHITESPACE = re.compile(r'\s+')


def load_customs_declarations():
    """Load the encoded boarding passes out of the text file.."""
    data = None
    with open("customs-responses.txt") as f:
        data = f.read()
    return data


def batch_declarations(declarations):
    """Split the declarations file into groups."""
    return declarations.split("\n\n")


def strip_response(response):
    """Nuke whitespace from orbit."""
    return re.sub(WHITESPACE, '', response)


def count_yes_questions(group):
    """How many questions got a yes from every person in the group.

    >>> count_yes_questions(['abc'])
    3
    >>> count_yes_questions(['abc', 'abc'])
    3
    >>> count_yes_questions(['a', 'b', 'c'])
    0
    >>> count_yes_questions(['ab', 'ac'])
    1
    >>> count_yes_questions(['a', 'a', 'a', 'a'])
    1
    >>> count_yes_questions(['b'])
    1
    """
    all_say_yes = set(strip_response(group[0]))
    if len(group) > 1:
        others = [strip_response(r) for r in group[1:]]
        all_say_yes.intersection_update(*others)
    return len(all_say_yes)


def solve_it():
    """Solve https://adventofcode.com/2020/day/6 puzzle 2."""
    groups = batch_declarations(load_customs_declarations())
    print(sum(count_yes_questions(group.split()) for group in groups))


if __name__ == "__main__":
    solve_it()
