"""Solver for Day 1, Problem 2 of Advent of Code 2020."""
import functools
import itertools
import operator


def solve_it():
    """Solve https://adventofcode.com/2020/day/1 puzzle."""
    with open("expense-report.txt") as f:
        expenses = (int(x) for x in f.readlines())
    triples = itertools.combinations(expenses, 3)
    my_man = [tr for tr in triples if sum(tr) == 2020][0]
    elves_need_this = functools.reduce(operator.mul, my_man, 1)
    print(elves_need_this)


if __name__ == "__main__":
    solve_it()
