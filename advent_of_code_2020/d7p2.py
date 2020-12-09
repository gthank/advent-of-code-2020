"""Solver for Day 7, Problem 2 of Advent of Code 2020."""
# import pprint
import re

from collections import deque
from functools import reduce
from operator import mul


EXTRACTOR = re.compile(r" ?(?P<count>\d+) (?P<bag_type>\w+ \w+) bags?")


def load_baggage_rules():
    """Load the baggage rules out of the text file.."""
    data = None
    with open("bag-rules.txt") as f:
        data = f.readlines()
    return [line.strip() for line in data]


def parse_rule(rule_text):
    """Parse ``rule_text`` to find container/containee relationships.

    >>> parse_rule('light r bags contain 1 bright w bag, 2 muted y bags.')
    ('light r', [(1, 'bright w'), (2, 'muted y')])

    >>> parse_rule('faded blue bags contain no other bags.')
    ('faded blue', [(0, 'no other bags')])
    """
    partitioned = rule_text.split("contain")
    container = partitioned[0].replace(" bags ", "").strip()
    contained = partitioned[1].replace(".", "")
    if contained.endswith("no other bags"):
        containees = [(0, "no other bags")]
    else:
        tokenized = contained.split(",")
        containees = []
        for token in tokenized:
            count = int(EXTRACTOR.match(token).group("count"))
            label = EXTRACTOR.match(token).group("bag_type")
            containees.append((count, label))
    return container, containees


def build_rules_dict(rules):
    """Turn the text rules into a dict of who can be contained by what.

    >>> rules = [
    ...   'l r bags contain 1 b w bag, 2 m y bags.',
    ...   'f b bags contain no other bags.']
    >>> build_rules_dict(rules)
    {'l r': [(1, 'b w'), (2, 'm y')], 'f b': [(0, 'no other bags')]}
    """
    containees_by_container = {}
    for rule in rules:
        container, containees = parse_rule(rule)
        containees_by_container[container] = containees
    # pp = pprint.PrettyPrinter()
    # pp.pprint(containees_by_container)
    return containees_by_container


def count_bags(rules_dict, bag_type="shiny gold"):
    """Figure out how many bags are inside my 'shiny gold' bag.

    >>> rules = [
    ...     'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    ...     'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    ...     'bright white bags contain 1 shiny gold bag.',
    ...     'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    ...     'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    ...     'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    ...     'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    ...     'faded blue bags contain no other bags.',
    ...     'dotted black bags contain no other bags.',
    ... ]
    >>> rules_dict = build_rules_dict(rules)
    >>> count_bags(rules_dict, 'shiny gold')
    33
    """
    inside = rules_dict[bag_type]
    # print(f"{bag_type} contains: {inside}")
    num_bags = 1  # Start at 1, because the current bag counts.
    for count, label in inside:
        if count == 0:
            return num_bags
        num_bags += count * count_bags(rules_dict, label)
    # print(f"{num_bags} inside {bag_type}.")
    return num_bags


def solve_it():
    """Solve https://adventofcode.com/2020/day/7 puzzle 2."""
    containees_by_container = build_rules_dict(load_baggage_rules())
    count = count_bags(containees_by_container)
    print(f"My shiny gold bag has {count - 1} other bags inside it.")


if __name__ == "__main__":
    solve_it()
