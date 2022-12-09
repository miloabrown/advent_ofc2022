"""
Advent Of code 2022
Code written by Milo
DAY8: Treetop Tree House
"""
with open("day_8/input.txt", "r") as file:
    data = [[int(x) for x in row.strip()] for row in file]


def is_edge(x, y):
    return x == 0 or y == 0 or x == len(data) - 1 or y == len(data) - 1


def is_visible(x, y):
    if is_edge(x, y):
        return True
    tree = data[x][y]

    def up(x, y):
        if data[x - 1][y] < tree and is_edge(x - 1, y):
            return True
        elif data[x - 1][y] < tree:
            return up(x - 1, y)
        else:
            return False

    def left(x, y):
        if data[x][y - 1] < tree and is_edge(x, y - 1):
            return True
        elif data[x][y - 1] < tree:
            return left(x, y - 1)
        else:
            return False

    def right(x, y):
        if data[x][y + 1] < tree and is_edge(x, y + 1):
            return True
        elif data[x][y + 1] < tree:
            return right(x, y + 1)
        else:
            return False

    def down(x, y):
        if data[x + 1][y] < tree and is_edge(x + 1, y):
            return True
        elif data[x + 1][y] < tree:
            return down(x + 1, y)
        else:
            return False

    return up(x, y) or down(x, y) or left(x, y) or right(x, y)


def part1():
    """
    PART1
    how many trees are visible

    Answer: 1785
    """
    sum = 0
    for x, row in enumerate(data):
        for y, _ in enumerate(row):
            if is_visible(x, y):
                sum += 1
    return sum


def scenic_score(x, y):
    if is_edge(x, y):
        return 0
    tree = data[x][y]
    tree_x = x
    tree_y = y

    def up(x, y):
        if data[x - 1][y] < tree and is_edge(x - 1, y):
            return abs(tree_x - (x - 1))
        elif data[x - 1][y] < tree:
            return up(x - 1, y)
        else:
            return abs(tree_x - (x - 1))

    def left(x, y):
        if data[x][y - 1] < tree and is_edge(x, y - 1):
            return abs(tree_y - (y - 1))
        elif data[x][y - 1] < tree:
            return left(x, y - 1)
        else:
            return abs(tree_y - (y - 1))

    def right(x, y):
        if data[x][y + 1] < tree and is_edge(x, y + 1):
            return abs(tree_y - (y + 1))
        elif data[x][y + 1] < tree:
            return right(x, y + 1)
        else:
            return abs(tree_y - (y + 1))

    def down(x, y):
        if data[x + 1][y] < tree and is_edge(x + 1, y):
            return abs(tree_x - (x + 1))
        elif data[x + 1][y] < tree:
            return down(x + 1, y)
        else:
            return abs(tree_x - (x + 1))

    return up(x, y) * down(x, y) * left(x, y) * right(x, y)


def part2():
    """
    PART2
    Whats the best scenic score

    Answer: 345168
    """

    maxi = 0
    for x, row in enumerate(data):
        for y, _ in enumerate(row):
            maxi = max(maxi, scenic_score(x, y))
    return maxi


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
