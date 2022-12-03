"""
Advent Of code 2022
Code written by Milo
"""

# Deal with input.
with open("day_1/input.txt", "r") as file:
    data = []
    elf = []
    for row in file:
        if row.strip().isnumeric():
            elf.append(int(row.strip()))
        else:
            data.append(elf.copy())
            elf.clear()


def part1():
    """
    PART1
    Find the elf carrying the most calories.
    Answer is the calories of this elf.
    # Answer for part1: 72017
    """
    return max([sum(elf) for elf in data])


def part2():
    """
    PART2
    Find the top3 elves carrying the most calories.
    The answer is the sum of the calories of these three.
    # Answer for part2: 212520
    """
    return sum(sorted([sum(elf) for elf in data], reverse=True)[:3])


def main():
    print(f"Part1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()
