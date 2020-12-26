"""Solver for Day 8, Problem 1 of Advent of Code 2020."""


def load_boot_code():
    """Read the boot code from the assembly dump.

    Will return a ``list`` of "instructions", i.e.,
    a 2-tuple of ``(opcode, arg)``.
    """
    boot_code = []
    with open("assembly.txt") as f:
        for line in f.readlines():
            opcode, arg = line.strip().split()
            arg = int(arg)
            boot_code.append((opcode, arg))
    return boot_code


def solve_it():
    """Solve https://adventofcode.com/2020/day/8 puzzle 1."""
    boot_code = load_boot_code()
    accumulator = 0
    instruction_ptr = 0
    visited_instructions = set()

    while instruction_ptr < len(boot_code):
        # EUREKA! I've solved the halting problem!!!
        if instruction_ptr in visited_instructions:
            break
        visited_instructions.add(instruction_ptr)

        opcode, arg = boot_code[instruction_ptr]
        if opcode == "nop":
            instruction_ptr += 1
        elif opcode == "jmp":
            instruction_ptr += arg
        elif opcode == "acc":
            accumulator += arg
            instruction_ptr += 1

    print(f"Accumulator = {accumulator}")


if __name__ == "__main__":
    solve_it()
