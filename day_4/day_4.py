"""
Advent Of code 2022
Code written by Milo
DAY4: Camp Cleanup
"""
with open("day_4/input.txt", "r") as file:
    data = [row.strip().split(",") for row in file]

# Convert data into tuple of ranges for each cleaning area pair
# --> data = [(range(1),range(2)),(range(1),range(2)),(...,...),...]
data = list(
    map(
        lambda x: (
            range(int(x[0].split("-")[0]), int(x[0].split("-")[1]) + 1),
            range(int(x[1].split("-")[0]), int(x[1].split("-")[1]) + 1),
        ),
        data,
    )
)
print(data[0])


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

    return sum([1 if is_sub(x[0], x[1]) else 0 for x in data])


def part2():
    """
    PART2
    How many pairs overlap

    Answer: 905
    """

    def overlaps(a, b):
        # Takes the two ranges as parameters and checks if they overlap
        return any(i in a for i in b)

    return sum([1 if overlaps(x[0], x[1]) else 0 for x in data])


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
