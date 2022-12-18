"""
Advent Of code 2022
Code written by Milo
DAY13: Distress Signal
"""

from ast import literal_eval
from functools import cmp_to_key
from math import prod

with open("day_13/input.txt", "r") as file:

    data = [
        [literal_eval(x) for x in pair.split("\n")]
        for pair in file.read().strip().split("\n\n")
    ]


def compare(left, right):
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    for left2, right2 in zip(left, right):
        if isinstance(left2, list) or isinstance(right2, list):
            rec = compare(left2, right2)
        else:
            rec = right2 - left2
        if rec != 0:
            return rec
    return len(right) - len(left)


def part1():
    """
    PART1
    sum of all indicies where left < right

    Answer: 6420
    """
    return sum(
        idx + 1
        for idx, value in enumerate([compare(x[0], x[1]) for x in data])
        if value > 0
    )


def part2():
    packets = sorted(
        [y for x in data for y in x] + [[[2]], [[6]]],
        key=cmp_to_key(compare),
        reverse=True,
    )
    return prod([x for x, packet in enumerate(packets, 1) if packet in ([[2]], [[6]])])


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
