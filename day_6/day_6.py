"""
Advent Of code 2022
Code written by Milo
DAY6: Tuning Trouble
"""
from itertools import count

with open("day_6/input.txt", "r") as file:
    data = file.read().strip()


def index_of_packet(size):
    return next(filter(lambda x: len(set(data[x - size : x])) == size, count()))


def part1():
    """
    PART1
    find where first start of packet (size 4) marker is detected

    Answer: 1651
    """
    return index_of_packet(4)


def part2():
    """
    PART2
    find where first start of packet (size 14) marker is detected

    Answer: 3837
    """
    return index_of_packet(14)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
