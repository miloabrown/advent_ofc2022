"""
Advent Of code 2022
Code written by Milo
DAY7: No Space Left On Device

test_input answer: 95437
"""


with open("day_7/input.txt", "r") as file:
    data = file.read().split("\n")


class Dir:
    def __init__(self, name, parent=None):
        self.__name = name
        self.__parent = parent
        self.__children = []
        self.__size = 0

    def get_name(self):
        return self.__name

    def add_parent(self, parent):
        self.__parent = parent

    def add_child(self, child):
        self.__children.append(child)

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def get_child(self, child):
        return next(filter(lambda x: x.get_name() == child, self.__children))

    def get_size(self):
        if not self.get_children():
            return self.__size
        else:
            return self.__size + sum(map(lambda x: x.get_size(), self.get_children()))

    def add_size(self, file_size):
        self.__size += int(file_size)


# Create tree structure
current = Dir(data[0].split(" ")[-1])
tree = [current]

for i in data[1:]:
    row = i.split(" ")

    # handle commands

    if row[-1] == "ls":
        continue

    elif row[1] == "cd":
        if row[-1] == "..":
            current = current.get_parent()
        else:
            current = current.get_child(row[-1])

    elif row[0] == "dir":
        child = Dir(row[-1], current)
        current.add_child(child)
        tree.append(child)

    elif row[0].isnumeric():
        current.add_size(row[0])


def part1():
    """
    PART1
    find all directories with size of 100000 at most
    and calculate their sum

    Answer: 1428881
    """

    return sum(dir.get_size() for dir in tree if dir.get_size() <= 100000)


def part2():
    """
    PART2
    what is the smallest directory that
    will free up enough space for update

    Answer:
    """

    to_delete = 30000000 - (70000000 - tree[0].get_size())
    return min([dir.get_size() for dir in tree if dir.get_size() >= to_delete])


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
