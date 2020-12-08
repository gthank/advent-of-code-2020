"""Solver for Day 7, Problem 1 of Advent of Code 2020."""
import re

from collections import defaultdict, deque


EXTRACTOR = re.compile(r" ?\d+ (?P<bag_type>\w+ \w+) bags?")


def load_baggage_rules():
    """Load the baggage rules out of the text file.."""
    data = None
    with open("bag-rules.txt") as f:
        data = f.readlines()
    return [line.strip() for line in data]


def parse_rule(rule_text):
    """Parse ``rule_text`` to find container/containee relationships.

    >>> parse_rule('light r bags contain 1 bright w bag, 2 muted y bags.')
    ('light r', ['bright w', 'muted y'])

    >>> parse_rule('faded blue bags contain no other bags.')
    ('faded blue', ['no other bags'])
    """
    partitioned = rule_text.split("contain")
    container = partitioned[0].replace(" bags ", "").strip()
    contained = partitioned[1].replace(".", "")
    if contained.endswith("no other bags"):
        containees = ["no other bags"]
    else:
        tokenized = contained.split(",")
        containees = [EXTRACTOR.match(t).group("bag_type") for t in tokenized]
    return container, containees


def build_rules_dict(rules):
    """Turn the text rules into a dict of who can be contained by what."""
    container_by_containees = defaultdict(set)
    for rule in rules:
        container, containees = parse_rule(rule)
        for c in containees:
            container_by_containees[c].add(container)
    return container_by_containees


def find_leaves(rules_dict):
    """Find distinct bag types that might contain a shiny gold bag."""
    leaves = set()
    q = deque(rules_dict["shiny gold"])
    while len(q) > 0:
        # Hit the next container in our queue.
        cur = q.popleft()
        # Add it to the list of bags that can contain a shiny gold bag within.
        leaves.add(cur)
        # Now add all the types of bags that can contain it to our list of bag
        # types to inspect, *IFF* we haven't already added them to the final
        # set (we could probably skip that check, but we know we'd just be
        # wasting work if processed any twice, so let's just leave it).
        for container in rules_dict[cur]:
            if container in leaves:
                continue
            q.append(container)
    return leaves


def solve_it():
    """Solve https://adventofcode.com/2020/day/7 puzzle 1."""
    containers_by_containee = build_rules_dict(load_baggage_rules())
    outermost_bags = find_leaves(containers_by_containee)
    count = len(outermost_bags)
    print(f"{count} types of bag might contain a shiny gold bag.")


if __name__ == "__main__":
    solve_it()
