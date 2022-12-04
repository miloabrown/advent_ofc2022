"""
Advent Of code 2022
Code written by Milo
DAY4: Camp Cleanup
"""
from itertools import chain

with open("day_4/input.txt", "r") as file:
    # Save data into list that contains each cleaning area pair as list of ranges:
    # --> data = [[range1,range2],[range3,range4],...]
    # this way ranges are easy to convert to sets for inspection
    # messy but works...
    data = [
        [
            range(int(x.split("-")[0]), int(x.split("-")[1]) + 1)
            for x in row.strip().split(",")
        ]
        for row in file
    ]


def part1():
    """
    PART1
    Check how many pairs contain the other

    Answer: 576
    """

    def is_sub(a, b):
        # Takes the two ranges as parameters and checks if
        # either one completely contains the other
        return set(a).issubset(b) or set(b).issubset(a)

    return sum([is_sub(x[0], x[1]) for x in data])


def part2():
    """
    PART2
    How many pairs overlap

    Answer: 905
    """

    def overlaps(a, b):
        # Takes the two ranges as parameters and checks if they overlap
        return any(i in a for i in b)

    return sum([overlaps(x[0], x[1]) for x in data])


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
