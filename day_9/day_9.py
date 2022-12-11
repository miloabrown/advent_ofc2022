"""
Advent Of code 2022
Code written by Milo
DAY9: Rope Bridge
"""
from numpy import sign

with open("day_9/input.txt", "r") as file:
    data = file.read().strip().split("\n")


def is_close(head, tail):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2


directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}


def move(dir, dist, knots, visited):
    for _ in range(int(dist)):
        knots[0][0] += directions[dir][0]
        knots[0][1] += directions[dir][1]

        for i in range(len(knots) - 1):
            if not is_close(knots[i], knots[i + 1]):
                knots[i + 1][0] += sign(knots[i][0] - knots[i + 1][0])
                knots[i + 1][1] += sign(knots[i][1] - knots[i + 1][1])

        visited.add(tuple(knots[len(knots) - 1]))


def solve(n):
    knots = [[0, 0] for x in range(n)]
    visited = set({(0, 0)})

    for step in data:
        dir, dist = step.split(" ")
        move(dir, dist, knots, visited)

    return len(visited)


def part1():
    """
    PART1
    how many spaces does the tail visit with two knots

    Answer: 5710
    """
    return solve(2)


def part2():
    """
    PART2
    how many spaces does the tail visit with 10 knots

    Answer: 2259
    """
    return solve(10)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
