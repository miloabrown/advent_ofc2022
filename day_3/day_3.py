"""
Advent Of code 2022
Code written by Milo
DAY3 Rucksack Reorganization
"""

from itertools import chain, zip_longest

with open("day_3/input.txt", "r") as file:
    data = [row.strip() for row in file]

priority = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1():
    """
    PART1
    2 compartments in rucksack
    Find priority of item that is in both compartments

    Answer: 7908
    """

    def find_shared_item(row):
        a = row[: len(row) // 2]
        b = row[len(row) // 2 :]
        return "".join(set(a).intersection(b))

    return sum(map(lambda x: priority.index(find_shared_item(x)), data))


def part2():
    """
    PART2
    find shared item in three-elf groups

    Answer: 2838
    """

    def find_shared_item(elf1, elf2, elf3):
        return "".join(set(elf1).intersection(elf2).intersection(elf3))

    def grouper(iterable, n, fillvalue=""):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue)

    return sum(
        map(
            lambda x: priority.index(find_shared_item(x[0], x[1], x[2])),
            grouper(chain(data), 3),
        )
    )


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
