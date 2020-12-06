"""Solver for Day 6, Problem 1 of Advent of Code 2020."""
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


def count_yes_questions(group):
    """How many questions got a yes from at least one person in the group."""
    all_answers = ''.join(group)
    no_spaces = re.sub(WHITESPACE, '', all_answers)
    return len(set(no_spaces))


def solve_it():
    """Solve https://adventofcode.com/2020/day/6 puzzle 1."""
    groups = batch_declarations(load_customs_declarations())
    print(f"Groups: {groups}")
    print(sum(count_yes_questions(group) for group in groups))


if __name__ == "__main__":
    solve_it()
