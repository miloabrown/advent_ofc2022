"""
Advent Of code 2022
Code written by Milo
DAY11: Monkey in the Middle
"""
from ast import literal_eval
from collections import deque
from math import prod

with open("day_11/input.txt", "r") as file:
    data = [x.split("\n") for x in file.read().strip().split("\n\n")]


def parse_monkey(
    info,
):  # Data in format: [[(int)Monkey id, (list)items, (str)operation, (tuple)test]]
    id = int(info[0].strip("Monkey :"))
    items = [int(x) for x in info[1][18:].split(", ")]
    operation = info[2][19:]
    test = (
        int(info[3][21:]),
        int(info[4][29:]),
        int(info[5][30:]),
    )
    return [id, items, operation, test]


data = list(map(lambda x: parse_monkey(x), data))


def find_monkey(id, monkeys):
    for monkey in monkeys:
        if monkey.get_id() == id:
            return monkey


class Monkey:
    def __init__(self, id, items, operation, test):
        self.id = id
        self.items = deque(items)
        self.operation = operation
        self.test = test
        self.inspected = 0

    def add_item(self, item):
        self.items.append(item)

    def get_inspected(self):
        return self.inspected

    def get_item(self):
        return self.items.popleft()

    def get_id(self):
        return self.id

    def get_items(self):
        return self.items

    def get_test_div(self):
        return self.test[0]

    def get_new(self, manager):
        self.inspected += 1
        old = self.items.popleft()
        return (
            eval(self.operation) // manager
            if manager == 3
            else eval(self.operation) % manager
        )

    def throw_item(self, monkeys, manager):
        div, t, f = self.test  # divisible by ? true : false
        item = self.get_new(manager)
        new = find_monkey(t, monkeys) if item % div == 0 else find_monkey(f, monkeys)
        new.add_item(item)

    def inspect_all(self, monkeys, manager):
        for _ in range(len(self.get_items())):
            self.throw_item(monkeys, manager)


def solve(rounds, manager):
    monkeys = [Monkey(x[0], x[1], x[2], x[3]) for x in data]

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect_all(monkeys, manager)

    return prod(sorted([x.get_inspected() for x in monkeys])[-2:])


def part1():
    """
    PART1
    monkey business after 20 rounds with "worry manager" 3

    Answer: 102399
    """
    return solve(rounds=20, manager=3)


def part2():
    """
    PART2
    monkey business after 10000
    with no initial "worry manager"

    Answer: 23641658401
    """

    m = prod([x[3][0] for x in data])

    return solve(10000, m)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
