"""
Advent Of code 2022
Code written by Milo
DAY2
"""
# handle input, list of rows in format [[A, B],[A, B], ...]
with open("day_2/input.txt", "r") as file:
    data = [row.strip().split(" ") for row in file]

"""
PART1
Rock paper Scissors:
First character in each row is what the opponent will play:
A: ROCK     :X
B: PAPER    :Y
C: SCISSORS :Z

Rounds can end in draw
Total score: Sum of each round
Round score =
Shape score: rock: 1, paper: 2, scissors: 3
+
Outcome score: lose: 0, 3: draw, 6: win
"""


def part1():
    def outcome_score(hand):
        if hand in [["A", "Y"], ["B", "Z"], ["C", "X"]]:
            return 6
        if hand in [["A", "Z"], ["B", "X"], ["C", "Y"]]:
            return 0
        else:
            return 3

    def shape_score(hand):
        score = {"X": 1, "Y": 2, "Z": 3}
        return score[hand[1]]

    def total_score(games):
        return sum(map(lambda game: outcome_score(game) + shape_score(game), games))

    return total_score(data)


def part2():
    pass


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
