"""
Advent Of code 2022
Code written by Milo
DAY4: Camp Cleanup
"""

with open("day_4/input.txt", "r") as file:
    data = [
        [(int(x.split("-")[0]), int(x.split("-")[1])) for x in row.strip().split(",")]
        for row in file
    ]


def part1():
    """
    PART1
    Check how many pairs contain the other

    Answer: 576
    """

    def is_sub(a, b):
        return (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1])

    return sum([is_sub(x[0], x[1]) for x in data])


def part2():
    """
    PART2
    How many pairs overlap

    Answer: 905
    """

    def overlaps(a, b):
        # Takes the two ranges as parameters and checks if they overlap
        return b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]

    return sum([overlaps(x[0], x[1]) for x in data])


def main():
    print(f"Part1: {(part1())}\n" f"Part2: {(part2())}")


if __name__ == "__main__":
    main()
