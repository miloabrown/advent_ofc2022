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

    Answer: 5710
    """

    head, tail = [0, 0], [0, 0]
    visited = []

    for step in data:

        dir, dist = step.split(" ")

        for _ in range(int(dist)):
            head[0] += directions[dir][0]
            head[1] += directions[dir][1]
            if not is_close(head[0], head[1], tail[0], tail[1]):
                tail[0], tail[1] = (
                    head[0] - directions[dir][0],
                    head[1] - directions[dir][1],
                )
            if [tail[0], tail[1]] not in visited:
                visited.append([tail[0], tail[1]])

    return len(visited)


def part2():
    """
    PART2

    Answer:
    """
    pass


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
