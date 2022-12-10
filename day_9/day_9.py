"""
Advent Of code 2022
Code written by Milo
DAY9: Rope Bridge
"""
with open("day_9/input.txt", "r") as file:
    data = file.read().strip().split("\n")


def is_close(head_row, head_col, tail_row, tail_col):
    return abs(head_row - tail_row) < 2 and abs(head_col - tail_col) < 2


directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}


def part1():
    """
    PART1
    how many spaces does the tail visit with two knots

    Answer: 5710
    """
    knots = [[0, 0], [0, 0]]
    visited = set()

    def move(head, next, dir, dist):
        for _ in range(int(dist)):
            head[0] += directions[dir][0]
            head[1] += directions[dir][1]
            if not is_close(head[0], head[1], next[0], next[1]):
                next[0], next[1] = (
                    head[0] - directions[dir][0],
                    head[1] - directions[dir][1],
                )
            visited.add((next[0], next[1]))

    for step in data:
        dir, dist = step.split(" ")
        move(knots[0], knots[1], dir, dist)

    return len(visited)


def part2():
    """
    PART2
    how many spaces does the tail visit with 10 knots

    Answer:
    """
    knots = [[0, 0] for x in range(10)]
    visited = set()


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
