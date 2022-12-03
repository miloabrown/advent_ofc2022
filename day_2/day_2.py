"""
Advent Of code 2022
Code written by Milo
DAY2
"""
# handle input, list of rows in format [[A, B],[A, B], ...]
with open("day_2/input.txt", "r") as file:
    data = [row.strip().split(" ") for row in file]


def outcome_score(hand):
    """returns the outcome score for given game"""
    if hand in [["A", "Y"], ["B", "Z"], ["C", "X"]]:
        return 6
    if hand in [["A", "Z"], ["B", "X"], ["C", "Y"]]:
        return 0
    else:
        return 3


def shape_score(hand):
    """returns the shape score for given game"""
    score = {"X": 1, "Y": 2, "Z": 3}
    return score[hand[1]]


def part1():
    """
    PART1
    Rock paper Scissors:
    First character in each row is what the opponent will play:
    A: ROCK     :X
    B: PAPER    :Y
    C: SCISSORS :Z

    Rounds can end in draw
    Total score: Sum of each round
    Round score
    =
    Shape score: rock: 1, paper: 2, scissors: 3
    +
    Outcome score: lose: 0, 3: draw, 6: win

    # Answer: 9241
    """

    def total_score(games):
        """returns total score of all games"""
        return sum(map(lambda game: outcome_score(game) + shape_score(game), games))

    return total_score(data)


def part2():
    """
    X: lose
    Y: draw
    Z: win
    Figure out what hand needs to be played,
    and calculate new score based on new hand.

    # Answer: 14610
    """

    def what_to_play(hand):
        moves = {
            "A": {"X": "Z", "Y": "X", "Z": "Y"},
            "B": {"X": "X", "Y": "Y", "Z": "Z"},
            "C": {"X": "Y", "Y": "Z", "Z": "X"},
        }
        return moves[hand[0]][hand[1]]

    def total_score(games):
        """returns total score of all games"""
        return sum(
            map(
                lambda game: outcome_score([game[0], what_to_play(game)])
                + shape_score([game[0], what_to_play(game)]),
                games,
            )
        )

    return total_score(data)


def main():
    print(f"Part1: {part1()}\n" f"Part2: {part2()}")


if __name__ == "__main__":
    main()
