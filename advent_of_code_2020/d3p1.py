"""Solver for Day 3, Problem 1 of Advent of Code 2020."""


def load_map():
    """Load the map to the airport."""
    my_map = []
    with open("map-to-airport.txt") as f:
        for line in f.readlines():
            line = [1 if x == "#" else 0 for x in line.strip()]
            my_map.append(line)
    return my_map


def solve_it():
    """Solve https://adventofcode.com/2020/day/3 puzzle."""
    my_map = load_map()
    x, y = 0, 0
    tree_count = 0
    while y < len(my_map):
        line = my_map[y]
        print(f"line is {len(line)} long.")
        spot = line[x]
        print(f"Current map line: {line}")
        print(f"Current position: ({x}, {y}) = {spot}")
        if spot == 1:
            tree_count += 1
        x, y = x + 3, y + 1
        # The pattern repeats ad infinitum to the right, so if we go past the
        # right edge of the map, then we can just wrap around.
        if x >= len(line):
            x -= len(line)
    print(f"{tree_count} trees in path.")


if __name__ == "__main__":
    solve_it()
