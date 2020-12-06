"""Solver for Day 5, Problem 1 of Advent of Code 2020."""


def load_boarding_passes():
    """Load the encoded boarding passes out of the text file.."""
    stripped = []
    with open("boarding-passes.txt") as f:
        stripped = [line.strip() for line in f.readlines()]
    return stripped


def calculate_row(boarding_pass):
    """Use boarding pass to figure out which row to sit in.

    >>> calculate_row('FBFBBFFRLR')
    44
    >>> calculate_row('BFFFBBFRRR')
    70
    >>> calculate_row('FFFBBBFRRR')
    14
    >>> calculate_row('BBFFBBFRLL')
    102

    ..NOTE: Feels like there should be a binary trick here, but it's too late
            for me to figure it out.
    """
    lower, upper = 0, 127
    for p in boarding_pass[:6]:
        if p == "F":
            upper = (lower + upper) // 2
        else:
            lower = 1 + (lower + upper) // 2
    if boarding_pass[6] == "F":
        return lower
    return upper


def calculate_seat(boarding_pass):
    """Use boarding pass to figure out which seat in the row to sit in.

    >>> calculate_seat('FBFBBFFRLR')
    5
    >>> calculate_seat('BFFFBBFRRR')
    7
    >>> calculate_seat('FFFBBBFRRR')
    7
    >>> calculate_seat('BBFFBBFRLL')
    4

    ..NOTE: Feels like there should be a binary trick here, but it's too late
            for me to figure it out.
    """
    lower, upper = 0, 7
    for p in boarding_pass[7:-1]:
        if p == "L":
            upper = (lower + upper) // 2
        else:
            lower = 1 + (lower + upper) // 2
    if boarding_pass[-1] == "L":
        return lower
    return upper


def calculate_seat_id(boarding_pass):
    """Calculate the seat_id for ``boarding_pass``.

    >>> calculate_seat_id('FBFBBFFRLR')
    357
    """
    return 8 * calculate_row(boarding_pass) + calculate_seat(boarding_pass)


def solve_it():
    """Solve https://adventofcode.com/2020/day/5 puzzle 1."""
    print(max((calculate_seat_id(bp) for bp in load_boarding_passes())))


if __name__ == "__main__":
    solve_it()
