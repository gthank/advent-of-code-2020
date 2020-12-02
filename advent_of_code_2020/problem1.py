"""Solver for Problem 1, Day 1 of Advent of Code 2020."""
import itertools


def solve_it():
    """Solve https://adventofcode.com/2020/day/1 puzzle."""
    with open("expense-report.txt") as f:
        expenses = (int(x) for x in f.readlines())
    pairs = itertools.combinations(expenses, 2)
    my_man = [p for p in pairs if sum(p) == 2020][0]
    print(my_man[0] * my_man[1])


if __name__ == "__main__":
    solve_it()
