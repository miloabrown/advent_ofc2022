"""
Advent Of code 2022
Code written by Milo
DAY5: Supply Stacks
"""
import copy
from collections import deque

with open("day_5/input.txt", "r") as file:
    data = file.readlines()

# Deal with initial stacks. Store them in a list of deques
stacks1 = [deque() for x in range(9)]
for row in data[:8]:
    for index, symbol in enumerate(row[1::4]):
        if symbol.isalpha():
            stacks1[index % 9].append(symbol)

# Deal with moves data
moves = [
    [
        int(row.strip().split(" ")[1]),
        int(row.strip().split(" ")[3]),
        int(row.strip().split(" ")[5]),
    ]
    for row in data[10:]
]


def top_crates(stacks):
    return "".join([x.popleft() if x else "" for x in stacks])


def part1():
    """
    PART1
    crane can only move one crate at a time
    what is the order of crates after all moves

    Answer: CNSZFDVLJ
    """

    def move(amount, stack1, stack2):
        for i in range(amount):
            stack2.appendleft(stack1.popleft())

    # Go through all moves
    for m in moves:
        move(m[0], stacks1[m[1] - 1], stacks1[m[2] - 1])

    return top_crates(stacks1)


# make a copy of stacks for part2
stacks2 = copy.deepcopy(stacks1)


def part2():
    """
    PART2
    crane can move multiple boxes

    Answer: QNDWLMGNS
    """

    def move(amount, stack1, stack2):
        temp_stack = []
        for i in range(amount):
            temp_stack.append(stack1.popleft())
        stack2.extendleft(reversed(temp_stack))

    # Go through all moves
    for m in moves:
        move(m[0], stacks2[m[1] - 1], stacks2[m[2] - 1])

    return top_crates(stacks2)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
