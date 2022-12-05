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
    row.strip()
    .replace("move ", "")
    .replace(" from ", " ")
    .replace(" to ", " ")
    .split(" ")
    for row in data[10:]
]

# make a copy of stack for part2
stacks2 = copy.deepcopy(stacks1)


def top_crates(stacks):
    ans = [x.popleft() if x else "" for x in stacks]
    return "".join(ans)


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
        move(int(m[0]), stacks1[int(m[1]) - 1], stacks1[int(m[2]) - 1])

    return top_crates(stacks1)


def part2():
    """
    PART2

    """

    def move(amount, stack1, stack2):
        temp_stack = []
        for i in range(amount):
            temp_stack.append(stack1.popleft())
        stack2.extendleft(reversed(temp_stack))

    # Go through all moves
    for m in moves:
        move(int(m[0]), stacks2[int(m[1]) - 1], stacks2[int(m[2]) - 1])

    return top_crates(stacks2)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
