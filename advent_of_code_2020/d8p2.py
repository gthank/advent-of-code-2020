"""Solver for Day 8, Problem 2 of Advent of Code 2020."""


def load_boot_code():
    """Read the boot code from the assembly dump.

    Will return a ``list`` of "instructions", i.e.,
    a 3-tuple of ``(instruction_number, opcode, arg)``.
    """
    boot_code = []
    with open("assembly.txt") as f:
        for instruction_number, line in enumerate(f.readlines()):
            opcode, arg = line.strip().split()
            arg = int(arg)
            boot_code.append((instruction_number, opcode, arg))
    return boot_code


def execute(
    program, instruction_ptr=0, accumulator=0, instruction_cache=None, allow_swap=True,
):
    """Execute the program, and return the value of the accumulator.

    If ``allow_swap`` is ``True``, then we will test the code as-is *and* with
    the next ``jump`` will be converted to a ``nop`` or the next ``nop`` will
    be converted to a ``jump``.

    If we detect a loop, we will return ``None`` to indicate that.

    >>> instructions = [
    ...      (1, 'nop', 0),
    ...      (2, 'acc', 1),
    ...      (3, 'jmp', 4),
    ...      (4, 'acc', 3),
    ...      (5, 'jmp', -3),
    ...      (6, 'acc', -99),
    ...      (7, 'acc', 1),
    ...      (8, 'jmp', -4),
    ...      (9, 'acc', 6),
    ... ]
    >>> execute(instructions)
    8
    """
    if instruction_cache is None:
        instruction_cache = set()

    # I'm pretty sure we just finished the program!
    if instruction_ptr == len(program):
        print("Finished successfully?")
        return accumulator
    elif instruction_ptr > len(program):
        # Error condition.
        print(f"Why is instruciton_ptr so big? {instruction_ptr}")
        return None

    instruction_number, opcode, arg = program[instruction_ptr]
    print(f"{instruction_number}: {opcode} {arg}")

    # Drat! Infinite loop detected.
    if f"{instruction_number}-{allow_swap}" in instruction_cache:
        print("I have some memory of this place.")
        return None

    # Guard against future infinite loop.
    instruction_cache.add(f"{instruction_number}-{allow_swap}")

    if opcode == "acc":
        accumulator += arg
        instruction_ptr += 1
        print(f"Accumulated. Proceed to {instruction_ptr}")
        return execute(
            program, instruction_ptr, accumulator, instruction_cache, allow_swap
        )

    if not allow_swap:
        if opcode == "nop":
            instruction_ptr += 1
            print(f"NOPd. Proceed to {instruction_ptr}")
            return execute(
                program, instruction_ptr, accumulator, instruction_cache, allow_swap
            )
        elif opcode == "jmp":
            instruction_ptr += arg
            print(f"JMP to {instruction_ptr}")
            return execute(
                program, instruction_ptr, accumulator, instruction_cache, allow_swap
            )
    else:
        if opcode == "nop":
            # Just do the "wrong" thing for the ops, and see if we get a valid result.
            print(f"Swap a NOP to a JMP to {instruction_ptr + arg}")
            altered = execute(
                program, instruction_ptr + arg, accumulator, instruction_cache, False
            )
            # If we didn't get back None (the error sentinel), return;
            # otherwise, continue with the instructions as-is and pass through
            # the allow_swap flag as-is.
            if altered is not None:
                print("It worked!")
                return altered

            print("Nuts!")
            return execute(
                program,
                instruction_ptr + 1,
                accumulator,
                instruction_cache,
                True,
            )
        elif opcode == "jmp":
            # Just do the "wrong" thing for the ops, and see if we get a valid result.
            print(f"Swap a JMP to a NOP to {instruction_ptr + arg}")
            altered = execute(
                program, instruction_ptr + 1, accumulator, instruction_cache, False
            )
            # If we didn't get back None (the error sentinel), return;
            # otherwise, continue with the instructions as-is and pass through
            # the allow_swap flag as-is.
            if altered is not None:
                print("It worked!")
                return altered

            print("Nuts!")
            return execute(
                program,
                instruction_ptr + arg,
                accumulator,
                instruction_cache,
                True,
            )

    # error condition
    print("MAJOR OOPSIE DETECTED!")
    return None


def solve_it():
    """Solve https://adventofcode.com/2020/day/8 puzzle 2."""
    boot_code = load_boot_code()
    accumulator = execute(boot_code)
    print(f"Accumulator = {accumulator}")


if __name__ == "__main__":
    solve_it()
