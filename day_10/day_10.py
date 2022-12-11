"""
Advent Of code 2022
Code written by Milo
DAY10: Cathode-Ray Tube
"""
with open("day_10/input.txt", "r") as file:
    data = file.read().strip().split("\n")


def part1():
    """
    PART1
    sum of signal strength during the
    20th,60th,100th,140th,180th,220th cycles

    Answer: 13060
    """
    values = {}
    x = 1
    cycle = 0
    for row in data:
        row = row.split(" ")

        if row[0] == "addx":
            for _ in range(2):
                cycle += 1
                values[cycle] = x * cycle
            x += int(row[1])
            continue

        cycle += 1
        values[cycle] = x * cycle

    return sum(values[i] for i in range(20, 221, 40))


def part2():
    """
    PART2
    print "#" if sprite in position and "."
    what are the four digits printed on the crt

    Answer: FJUBULRZ
    """

    x = 1
    cycle = 0
    pixels = list("." * 40 * 6)

    def draw_pixel(x, cycles, pixels):
        pixels[cycle - 1] = "#" if (cycle - 1) % 40 in range(x - 1, x + 2) else " "

    for row in data:
        row = row.split(" ")

        if row[0] == "addx":
            for _ in range(2):
                cycle += 1
                draw_pixel(x, cycle, pixels)
            x += int(row[1])
            continue
        cycle += 1
        draw_pixel(x, cycle, pixels)

    return ["".join(pixels[i : i + 40]) for i in range(0, 201, 40)]


def main():
    print(f"Part1: {part1()}\n" f"Part2:")
    print(*part2(), sep="\n")


if __name__ == "__main__":
    main()
