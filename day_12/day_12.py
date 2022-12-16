"""
Advent Of code 2022
Code written by Milo
DAY12: Hill Climbing Algorithm
"""


import numpy as np

with open("day_12/input.txt", "r") as file:
    data = np.array([list(row.strip()) for row in file])


def solve(start, end):
    start = np.argwhere(data == start)
    end = np.argwhere(data == end)
    queue = [(x, y, 0, "a") for x, y in start]
    visited = {(x, y) for x, y, *_ in queue}

    def find_path(x, y, path, current_level):
        if not 0 <= x < len(data) or not 0 <= y < len(data[x]) or (x, y) in visited:
            return
        next_node = data[x][y].replace("E", "z")
        if ord(next_node) > ord(current_level) + 1:
            return
        visited.add((x, y))
        queue.append((x, y, path + 1, next_node))

    while queue:
        x, y, path, current_level = queue.pop(0)
        if (x, y) == (end[0][0], end[0][1]):
            return path
        for n in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            find_path(n[0], n[1], path, current_level)


def part1():
    """
    PART1
    fewest steps required to get from S to E

    Answer: 339
    """
    return solve("S", "E")


def part2():
    """
    PART2
    fewest steps from the nearest "a" to end point

    Answer: 332
    """
    return solve("a", "E")


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
