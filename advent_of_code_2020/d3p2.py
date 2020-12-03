"""Solver for Day 3, Problem 1 of Advent of Code 2020."""
from functools import reduce
from operator import mul


def load_map():
    """Load the map to the airport."""
    my_map = []
    with open("map-to-airport.txt") as f:
        for line in f.readlines():
            line = [1 if x == "#" else 0 for x in line.strip()]
            my_map.append(line)
    return my_map


def count_trees(mappy_map, stride_x, stride_y):
    """Count trees on the slope defined by ``stride_y/stride_x``."""
    x, y = 0, 0
    tree_count = 0
    while y < len(mappy_map):
        line = mappy_map[y]
        spot = line[x]
        if spot == 1:
            tree_count += 1
        x, y = x + stride_x, y + stride_y
        # The pattern repeats ad infinitum to the right, so if we go past the
        # right edge of the map, then we can just wrap around.
        if x >= len(line):
            x -= len(line)
    return tree_count


def solve_it():
    """Solve https://adventofcode.com/2020/day/3 puzzle."""
    my_map = load_map()
    strides_to_calculate = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    tree_counts = []
    for x, y in strides_to_calculate:
        num_trees = count_trees(my_map, x, y)
        print(f"{num_trees} on slope: {x}, {y}")
        tree_counts.append(num_trees)
    product = reduce(mul, tree_counts, 1)
    print(product)


if __name__ == "__main__":
    solve_it()
